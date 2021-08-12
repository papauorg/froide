# Generated by Django 2.2.4 on 2020-03-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("publicbody", "0027_auto_20191001_1644"),
    ]

    operations = [
        migrations.AddField(
            model_name="publicbody",
            name="extra_data",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name="publicbody",
            name="source_reference",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="source reference"
            ),
        ),
    ]
