# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-21 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import filingcabinet.models


class Migration(migrations.Migration):

    dependencies = [
        ("document", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="pdf_file",
            field=models.FileField(
                blank=True,
                max_length=255,
                upload_to=filingcabinet.models.get_document_path,
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="image",
            field=models.ImageField(max_length=255, upload_to=""),
        ),
        migrations.AlterField(
            model_name="page",
            name="image_large",
            field=models.ImageField(max_length=255, upload_to=""),
        ),
        migrations.AlterField(
            model_name="page",
            name="image_normal",
            field=models.ImageField(max_length=255, upload_to=""),
        ),
        migrations.AlterField(
            model_name="page",
            name="image_thumbnail",
            field=models.ImageField(max_length=255, upload_to=""),
        ),
    ]
