# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 03:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msgboard', '0002_remove_msgpost_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='msgpost',
            options={},
        ),
        migrations.RemoveField(
            model_name='msgpost',
            name='datetime',
        ),
    ]
