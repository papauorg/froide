# Generated by Django 2.2.4 on 2019-10-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0020_auto_20191014_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='allow_annotation',
            field=models.BooleanField(default=False),
        ),
    ]
