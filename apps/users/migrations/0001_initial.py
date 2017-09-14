# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-11 15:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='\u8f6e\u64ad\u56fe')),
                ('url', models.URLField(verbose_name='\u8bbf\u95ee\u5730\u5740')),
                ('index', models.IntegerField(default=100, verbose_name='\u987a\u5e8f')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8f6e\u64ad\u56fe',
                'verbose_name_plural': '\u8f6e\u64ad\u56fe',
            },
        ),
    ]
