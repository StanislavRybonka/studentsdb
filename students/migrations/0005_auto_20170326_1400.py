# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-26 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20170301_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Foto'),
        ),
    ]
