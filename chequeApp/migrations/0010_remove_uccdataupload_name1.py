# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-20 12:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chequeApp', '0009_uccdataupload_name1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uccdataupload',
            name='name1',
        ),
    ]
