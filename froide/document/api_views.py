from django.db.models import Q, Value, BooleanField, Case, When
from django.utils.decorators import method_decorator

from rest_framework import serializers, permissions, viewsets

from filingcabinet.api_serializers import (
    DocumentSerializer as FCDocumentSerializer,
    PageSerializer as FCPageSerializer,
    DocumentCollectionSerializer as FCDocumentCollectionSerializer,
    UpdateDocumentSerializer,
    PagesMixin,
)
from filingcabinet.api_views import (
    DocumentViewSet as FCDocumentViewSet,
    DocumentCollectionViewSet as FCDocumentCollectionViewSet,
    PageAnnotationViewSet as FCPageAnnotationViewSet,
)
from filingcabinet.models import Page, PageAnnotation

from froide.helper.auth import can_write_object, get_read_queryset, get_write_queryset
from froide.helper.api_utils import SearchFacetListSerializer
from froide.helper.search.api_views import ESQueryMixin
from froide.helper.cache import cache_anonymous_page

from .models import Document, DocumentCollection
from .documents import PageDocument
from .filters import PageDocumentFilterset, get_document_read_qs, DocumentFilter


class DocumentSerializer(FCDocumentSerializer):
    file_url = serializers.CharField(source="get_authorized_file_url", read_only=True)
    original = serializers.HyperlinkedRelatedField(
        view_name="api:attachment-detail",
        lookup_field="pk",
        read_only=True,
    )
    foirequest = serializers.HyperlinkedRelatedField(
        view_name="api:request-detail",
        lookup_field="pk",
        read_only=True,
    )
    publicbody = serializers.HyperlinkedRelatedField(
        view_name="api:publicbody-detail",
        lookup_field="pk",
        read_only=True,
    )

    class Meta:
        model = Document
        fields = FCDocumentSerializer.Meta.fields + (
            "original",
            "foirequest",
            "publicbody",
        )


class DocumentDetailSerializer(PagesMixin, DocumentSerializer):
    pages = serializers.SerializerMethodField(source="get_pages")

    class Meta(DocumentSerializer.Meta):
        fields = DocumentSerializer.Meta.fields + ("pages",)


class DocumentCollectionSerializer(FCDocumentCollectionSerializer):
    class Meta:
        model = DocumentCollection
        fields = FCDocumentCollectionSerializer.Meta.fields


class AllowedOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if can_write_object(obj, request):
            return True
        if request.method in permissions.SAFE_METHODS and hasattr(obj, "public"):
            return obj.public

        return False


class PageSerializer(FCPageSerializer):
    query_highlight = serializers.CharField()

    class Meta(FCPageSerializer.Meta):
        fields = FCPageSerializer.Meta.fields + ("query_highlight",)
        list_serializer_class = SearchFacetListSerializer


class PageViewSet(ESQueryMixin, viewsets.GenericViewSet):
    serializer_class = PageSerializer
    search_model = Page
    search_document = PageDocument
    read_token_scopes = ["read:document"]
    searchfilterset_class = PageDocumentFilterset

    def list(self, request, *args, **kwargs):
        return self.search_view(request)

    def optimize_query(self, qs):
        return qs.prefetch_related("document")

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        if hasattr(self, "sqs"):
            ctx["facets"] = self.sqs.get_aggregations()
        return ctx


class DocumentViewSet(FCDocumentViewSet):
    serializer_action_classes = {
        "list": DocumentSerializer,
        "retrieve": DocumentDetailSerializer,
        "update": UpdateDocumentSerializer,
    }
    filterset_class = DocumentFilter

    def get_base_queryset(self):
        return get_document_read_qs(self.request, detail=self.action == "retrieve")

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related("original")

    @method_decorator(cache_anonymous_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class DocumentCollectionViewSet(FCDocumentCollectionViewSet):
    serializer_action_classes = {
        "list": DocumentCollectionSerializer,
        "retrieve": DocumentCollectionSerializer,
    }

    def get_queryset(self):
        if self.action == "list":
            public_q = Q(public=True, listed=True)
        else:
            public_q = Q(public=True)
        return get_read_queryset(
            DocumentCollection.objects.all(),
            self.request,
            has_team=True,
            public_q=public_q,
            scope="read:document",
        )

    @method_decorator(cache_anonymous_page(60 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PageAnnotationViewSet(FCPageAnnotationViewSet):
    permission_classes = (AllowedOrReadOnly,)

    def get_base_queryset(self, document_id):
        docs = Document.objects.all()
        try:
            doc = docs.get(pk=document_id)
        except (ValueError, Document.DoesNotExist):
            return PageAnnotation.objects.none()
        if not doc.can_read(self.request):
            return PageAnnotation.objects.none()
        return PageAnnotation.objects.filter(page__document=doc)

    def annotate_permissions(self, qs):
        write_qs = get_write_queryset(
            qs,
            self.request,
            has_team=False,
        )

        qs = qs.annotate(
            can_delete=Case(
                When(id__in=write_qs, then=Value(True)),
                default=Value(False),
                output_field=BooleanField(),
            )
        )
        return qs
