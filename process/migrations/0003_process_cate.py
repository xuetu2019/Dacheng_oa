# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-06-25 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0002_process_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='cate',
            field=models.CharField(max_length=50, null=True, verbose_name='部门'),
        ),
    ]
