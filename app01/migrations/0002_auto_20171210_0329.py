# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='预定的时间'),
        ),
    ]
