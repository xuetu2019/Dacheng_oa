# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-06-25 07:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_auto_20200624_1444'),
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admins.Admins'),
        ),
    ]