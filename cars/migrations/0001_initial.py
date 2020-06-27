# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-06-09 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=15, verbose_name='车牌')),
                ('department', models.CharField(max_length=30, verbose_name='线路')),
                ('state', models.CharField(max_length=15, verbose_name='状态')),
                ('age', models.IntegerField(max_length=3, verbose_name='车龄')),
                ('buy_time', models.DateField(verbose_name='购买日期')),
                ('logo', models.CharField(max_length=30, verbose_name='品牌')),
                ('sites', models.IntegerField(max_length=3, verbose_name='座位')),
                ('check', models.DateField(verbose_name='检车日期')),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]