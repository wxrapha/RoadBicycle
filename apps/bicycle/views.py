# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from .models import Brand, Bicycleclassify, ClassifyList
from teams.models import Teams
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class BrandView(View):
    def get(self, request, brand_id):
        brandlist = Brand.objects.all()
        teamslist = Teams.objects.all()
        branddesc = Brand.objects.get(id=int(brand_id))
        return render(request, 'brand.html', {
            'brandlist': brandlist,
            'teamslist': teamslist,
            'branddesc': branddesc
        })


class BicycleListView(View):
    def get(self, request, branddesc_id):
        brandlist = Brand.objects.all()
        teamslist = Teams.objects.all()
        classitylist = Bicycleclassify.objects.filter(brand_id=int(branddesc_id))
        bicyclelist = ClassifyList.objects.filter(brand_id=int(branddesc_id))
        bicycleclassitylist = ClassifyList.objects.filter(brand_id=int(branddesc_id))
        #对公路车进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(bicyclelist, 6, request=request)

        bicycles = p.page(page)

        return render(request, 'bicycle_list.html', {
            'brandlist': brandlist,
            'teamslist': teamslist,
            'classitylist': classitylist,
            'bicyclelist': bicycles,
            'bcl': bicycleclassitylist
        })