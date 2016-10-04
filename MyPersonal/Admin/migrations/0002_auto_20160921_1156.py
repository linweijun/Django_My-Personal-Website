# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('file', models.ImageField(upload_to='/media/')),
            ],
        ),
        migrations.RemoveField(
            model_name='dec_info',
            name='userId',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='userid',
        ),
        migrations.RemoveField(
            model_name='work_ex',
            name='userid',
        ),
        migrations.RemoveField(
            model_name='works',
            name='userid',
        ),
        migrations.DeleteModel(
            name='dec_info',
        ),
        migrations.DeleteModel(
            name='tags',
        ),
        migrations.DeleteModel(
            name='work_ex',
        ),
        migrations.DeleteModel(
            name='works',
        ),
    ]