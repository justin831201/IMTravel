# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-31 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0015_auto_20161002_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='category',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
