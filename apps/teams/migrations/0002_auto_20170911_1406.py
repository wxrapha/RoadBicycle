# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-11 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='team_name',
            field=models.CharField(default='', max_length=40, verbose_name='\u8f66\u961f'),
        ),
    ]