# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0005_auto_20170504_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasource',
            name='data_provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_loader.DataProvider'),
        ),
    ]
