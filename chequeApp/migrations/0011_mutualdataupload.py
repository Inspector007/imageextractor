# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-15 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chequeApp', '0010_remove_uccdataupload_name1'),
    ]

    operations = [
        migrations.CreateModel(
            name='MutualDataUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mutualfile', models.FileField(upload_to='document/mutualequity/')),
            ],
        ),
    ]
