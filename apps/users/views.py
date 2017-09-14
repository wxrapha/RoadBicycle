# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from .models import Banner
from teams.models import Teams
from bicycle.models import Brand
# Create your views here.


class IndexView(View):
    def get(self, request):

        brandlist = Brand.objects.all()
        teamslist = Teams.objects.all()
        all_banners = Banner.objects.all()
        return render(request, 'index.html', {
            'all_banners': all_banners,
            'teamslist': teamslist,
            'brandlist': brandlist
        })



