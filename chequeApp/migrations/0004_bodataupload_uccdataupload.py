# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-26 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chequeApp', '0003_auto_20160818_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoDataUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bofile', models.FileField(upload_to='document/bo/%m/%y/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='UccDataUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uccfile', models.FileField(upload_to='document/ucc/%m/%y/%d/')),
            ],
        ),
    ]