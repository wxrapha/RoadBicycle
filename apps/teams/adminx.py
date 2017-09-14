# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/9/11 上午10:04'

import xadmin

from .models import Teams, TeamMember


class TeamsAdmin(object):
    pass


class TeamMemberAdmin(object):
    list_display = ['name', 'team', 'detail', 'position']
    search_fields = ['name', 'team', 'detail', 'position']
    list_filter = ['name', 'team', 'detail', 'position']


xadmin.site.register(TeamMember, TeamMemberAdmin)
xadmin.site.register(Teams, TeamsAdmin)

