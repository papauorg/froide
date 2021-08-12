# Generated by Django 3.0.7 on 2020-06-22 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("document", "0022_auto_20200117_2101"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="outline",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="document",
            name="properties",
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
