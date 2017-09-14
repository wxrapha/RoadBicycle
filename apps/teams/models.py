# _*_ coding: utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from bicycle.models import Brand


# Create your models here.


class Teams(models.Model):
    team_name = models.CharField(max_length=40, verbose_name=u'车队', default='')
    detail = models.TextField(verbose_name=u'车队详情', null=True)
    image = models.ImageField(upload_to='teams/%Y/%m', verbose_name=u'车队图', max_length=100, null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'车队'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.team_name


class TeamMember(models.Model):
    team = models.ForeignKey(Teams, verbose_name='车队')
    name = models.CharField(max_length=100, verbose_name=u'姓名')
    position = models.CharField(verbose_name=u'定位', choices=(('gc', u'GC车手'), ('fj', u'副将'), ('cj',u'冲刺')), max_length=5)
    detail = models.TextField(max_length=300, verbose_name=u'详情')
    image = models.ImageField(upload_to='TeamMember/%Y/%m', verbose_name=u'照片', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'队员'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

