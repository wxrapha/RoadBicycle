# _*_ coding: utf-8 _*_
from django.conf.urls import url, include
from django.contrib import admin
import xadmin

from django.views.static import serve
from RoadBicycle.settings import MEDIA_ROOT
from users.views import IndexView, LoginView, RegisterView, ActiveUserView, LogoutView, ForgetPwdView, ResetView,\
                        ModifyPwdView
from teams.views import TeamsDetailView, MemberListView
from bicycle.views import BrandView, BicycleListView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^teams/(?P<team_id>\d+)$', TeamsDetailView.as_view(), name='teams'),

    url(r'^brand/(?P<brand_id>\d+)$', BrandView.as_view(), name='brand'),

    url(r'^bicycle/(?P<branddesc_id>\d+)$', BicycleListView.as_view(), name='bicycle_list'),

    url(r'^memberlist/(?P<team_id>\d+)$', MemberListView.as_view(), name='member_list'),
    #配置上传文件访问地址
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url('^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^forgetpwd/$', ForgetPwdView.as_view(), name='forgetpwd'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),
]
