# Generated by Django 3.0.8 on 2020-07-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("publicbody", "0028_auto_20200318_1415"),
    ]

    operations = [
        migrations.AddField(
            model_name="publicbody",
            name="change_proposals",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="publicbody",
            name="wikidata_item",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="Wikidata item"
            ),
        ),
    ]
