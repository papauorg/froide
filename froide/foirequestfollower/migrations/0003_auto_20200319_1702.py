# Generated by Django 2.2.4 on 2020-03-19 16:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foirequestfollower', '0002_auto_20191024_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='foirequestfollower',
            name='context',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foirequestfollower',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Timestamp of Following'),
        ),
    ]
