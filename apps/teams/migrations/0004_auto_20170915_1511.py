# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-15 15:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20170911_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teams',
            old_name='team_name',
            new_name='teamname',
        ),
    ]