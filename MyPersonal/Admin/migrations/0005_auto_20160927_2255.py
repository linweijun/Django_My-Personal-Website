# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_auto_20160921_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=254, unique=True, verbose_name='\u6807\u9898'),
        ),
    ]