# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/9/11 下午3:08'

import xadmin
from xadmin import views
from .models import Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = 'xiehao.pro'
    site_footer = 'xiehao'
    menu_style = 'accordion'


class BannerAdmin(object):
    pass

xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)