# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-26 09:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("publicbody", "0021_proposedpublicbody"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="proposedpublicbody",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "Proposed Public Body",
                "verbose_name_plural": "Proposed Public Bodies",
            },
        ),
    ]
