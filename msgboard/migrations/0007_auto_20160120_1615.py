# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 08:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msgboard', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='msg_id',
        ),
    ]
