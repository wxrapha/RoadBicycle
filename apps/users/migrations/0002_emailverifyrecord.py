# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-24 16:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='\u9a8c\u8bc1\u7801')),
                ('email', models.EmailField(max_length=50, verbose_name='\u90ae\u7bb1')),
                ('send_type', models.CharField(choices=[('register', '\u6ce8\u518c'), ('forget', '\u627e\u56de\u5bc6\u7801'), ('update_email', '\u4fee\u6539\u90ae\u7bb1')], max_length=30, verbose_name='\u9a8c\u8bc1\u7801\u7c7b\u578b')),
                ('send_time', models.DateField(default=datetime.datetime.now, verbose_name='\u53d1\u9001\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u90ae\u7bb1\u9a8c\u8bc1\u7801',
                'verbose_name_plural': '\u90ae\u7bb1\u9a8c\u8bc1\u7801',
            },
        ),
    ]
