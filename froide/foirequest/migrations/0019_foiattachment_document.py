# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-21 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("foirequest", "0018_requestdraft_law_type"),
        ("document", "0009_document_original"),
        ("filingcabinet", "__first__"),
    ]

    operations = [
        migrations.AddField(
            model_name="foiattachment",
            name="document",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="document.Document",
            ),
        ),
    ]
