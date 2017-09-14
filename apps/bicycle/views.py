from django.shortcuts import render
from django.views.generic.base import View
from .models import Brand, Bicycleclassify, ClassifyList
from teams.models import Teams
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
    def get(self, request):
        brandlist = Brand.objects.all()
        teamslist = Teams.objects.all()
        bicyclelist = ClassifyList.objects.all()
        classitylist = Bicycleclassify.objects.all()

        return render(request, 'bicycle_list.html', {
            'brandlist': brandlist,
            'teamslist': teamslist,
            'classitylist': classitylist,
            'bicyclelist': bicyclelist
        })