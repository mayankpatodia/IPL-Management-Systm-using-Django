# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20161206_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='cover_url',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo_url',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
