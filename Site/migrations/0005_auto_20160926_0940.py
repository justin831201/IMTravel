# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-26 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0004_auto_20160820_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='latitude',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='site',
            name='longitude',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
    ]
