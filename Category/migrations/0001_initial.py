# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_name', models.CharField(max_length=10)),
                ('english_name', models.CharField(max_length=20)),
            ],
        ),
    ]
