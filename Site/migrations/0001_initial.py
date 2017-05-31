# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 06:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
        ('Country', '0002_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_name', models.CharField(max_length=20)),
                ('english_name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.Category')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Country.Region')),
            ],
        ),
    ]
