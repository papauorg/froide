# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 14:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import oauth2_provider.generators
import oauth2_provider.validators


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0011_auto_20171106_1503"),
    ]

    operations = [
        migrations.CreateModel(
            name="Application",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "client_id",
                    models.CharField(
                        db_index=True,
                        default=oauth2_provider.generators.generate_client_id,
                        max_length=100,
                        unique=True,
                    ),
                ),
                (
                    "redirect_uris",
                    models.TextField(
                        blank=True,
                        help_text="Allowed URIs list, space separated",
                        validators=[oauth2_provider.validators.URIValidator],
                    ),
                ),
                (
                    "client_type",
                    models.CharField(
                        choices=[
                            ("confidential", "Confidential"),
                            ("public", "Public"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "authorization_grant_type",
                    models.CharField(
                        choices=[
                            ("authorization-code", "Authorization code"),
                            ("implicit", "Implicit"),
                            ("password", "Resource owner password-based"),
                            ("client-credentials", "Client credentials"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "client_secret",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        default=oauth2_provider.generators.generate_client_secret,
                        max_length=255,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255)),
                ("skip_authorization", models.BooleanField(default=False)),
                ("description", models.TextField(blank=True)),
                ("homepage", models.CharField(blank=True, max_length=255)),
                ("image_url", models.CharField(blank=True, max_length=255)),
                ("auto_approve_scopes", models.TextField(blank=True)),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="account_application",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
