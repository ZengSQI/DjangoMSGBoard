# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 03:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('msgboard', '0003_auto_20160119_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='msgpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 19, 3, 20, 21, 972772, tzinfo=utc)),
        ),
    ]