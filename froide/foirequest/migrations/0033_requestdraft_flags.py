# Generated by Django 2.1.4 on 2019-01-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foirequest", "0032_auto_20181115_1339"),
    ]

    operations = [
        migrations.AddField(
            model_name="requestdraft",
            name="flags",
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
