# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-30 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170530_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
    ]