# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/9/11 上午10:51'

import xadmin
from .models import Brand, Bicycleclassify, ClassifyList


class BrandAdmin(object):
    list_display = ['name', 'detail']


class BicycleclassifyAdmin(object):
    list_display = ['name', 'brand']
    search_fields = ['name', 'brand']
    list_filter = ['name', 'brand']


class ClassifyListAdmin(object):
    list_display = ['name', 'brand', 'classify', 'material']
    search_fields = ['name', 'brand', 'classify', 'material']
    list_filter = ['name', 'brand', 'classify', 'material']


xadmin.site.register(Brand, BrandAdmin)
xadmin.site.register(Bicycleclassify, BicycleclassifyAdmin)
xadmin.site.register(ClassifyList, ClassifyListAdmin)
