# Generated by Django 2.1.9 on 2019-06-24 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_fsm
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Upload",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "guid",
                    models.UUIDField(
                        default=uuid.uuid4, unique=True, verbose_name="GUID"
                    ),
                ),
                ("state", django_fsm.FSMField(default="initial", max_length=50)),
                ("upload_offset", models.BigIntegerField(default=0)),
                ("upload_length", models.BigIntegerField(default=-1)),
                ("upload_metadata", models.TextField(blank=True)),
                ("filename", models.CharField(blank=True, max_length=255)),
                ("temporary_file_path", models.CharField(max_length=4096, null=True)),
                ("expires", models.DateTimeField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
