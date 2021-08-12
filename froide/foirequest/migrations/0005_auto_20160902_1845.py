# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-02 16:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("foirequest", "0004_foirequest_is_blocked"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="foirequest",
            options={
                "get_latest_by": "last_message",
                "ordering": ("-last_message",),
                "permissions": (("see_private", "Can see private requests"),),
                "verbose_name": "Freedom of Information Request",
                "verbose_name_plural": "Freedom of Information Requests",
            },
        ),
    ]
