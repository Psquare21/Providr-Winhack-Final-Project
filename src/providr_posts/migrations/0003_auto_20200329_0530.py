# Generated by Django 3.0 on 2020-03-29 05:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providr_posts', '0002_auto_20200329_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 29, 5, 30, 57, 20852)),
        ),
    ]
