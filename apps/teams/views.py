from django.shortcuts import render
from django.views.generic.base import View
from .models import Teams, TeamMember
from bicycle.models import Brand
# Create your views here.


class TeamsDetailView(View):
    def get(self, request, team_id):
        brandlist = Brand.objects.all()
        teamlist = Teams.objects.all()
        teamdesc = Teams.objects.get(id=int(team_id))
        return render(request, 'team.html', {
            'teamsdesc': teamdesc,
            'teamslist': teamlist,
            'brandlist': brandlist
        })


class MemberListView(View):
    def get(self, request, team_id):
        memberslist = TeamMember.objects.get(id=int(team_id))
        brandlist = Brand.objects.all()
        teamlist = Teams.objects.all()
        return render(request, 'member_list.html', {
            'teamslist': teamlist,
            'brandlist': brandlist,
            'memberslist': memberslist

        })


