# _*_ coding: utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(verbose_name=u'品牌名称', max_length=20)
    detail = models.TextField(verbose_name=u'品牌介绍')
    image = models.ImageField(upload_to='Brand/%Y/%m', verbose_name=u'图片')


    class Meta:
        verbose_name = u'品牌'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Bicycleclassify(models.Model):
    name = models.CharField(verbose_name=u'品牌系列', max_length=20)
    brand = models.ForeignKey(Brand, verbose_name=u'品牌')
    category = models.CharField(verbose_name=u'定位', choices=
        (('dz', u'大组车'), ('tt', u'计时车'), ('yy', u'越野'),('tz', u'铁三'), ('xx', u'休闲')), max_length=5)
    image = models.ImageField(upload_to='RoadBicycle/%Y/%m', verbose_name=u'系列封面图')
    detail = models.TextField(max_length=300, verbose_name=u'介绍')
    add_time = models.TimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'系列'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class ClassifyList(models.Model):
    name = models.CharField(verbose_name=u'型号', max_length=50)
    brand = models.ForeignKey(Brand, verbose_name=u'品牌', null=True)
    classify = models.ForeignKey(Bicycleclassify, verbose_name=u'系列')
    material = models.CharField(verbose_name=u'材料', choices=
    (('tx', u'碳纤维'), ('lhj', u'铝合金'), ('gj', '钢')), max_length=5)
    image = models.ImageField(upload_to='RoadBicycleName/%Y/%m', verbose_name=u'图片')
    price = models.CharField(max_length=10, verbose_name=u'价格', default='')
    detail = models.TextField(verbose_name=u'介绍')
    add_time = models.TimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'型号'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
