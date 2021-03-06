# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-20 14:23
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0018_auto_20170614_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='spreadsheetsdatasource',
            name='field_list',
            field=jsonfield.fields.JSONField(default={}, verbose_name='Embulk-related set of fields serialized into JSON-format. Default schema is column_name:column_type'),
        ),
    ]
