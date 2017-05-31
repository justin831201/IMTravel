from django.shortcuts import render
from rest_framework import generics
from API.apis import SiteSerializer, SearchSerializer
from Site.models import Site
from Category.models import Category
from Site.function import keywordOfSites, scoreOfSites, productOfSite
from pymongo import MongoClient
# Create your views here.

class siteDetail(generics.ListAPIView):
    serializer_class = SiteSerializer
    model = serializer_class.Meta.model
    def get_queryset(self):
        divide = 1
        if 'id' in self.request.GET and self.request.GET['id'] != "":
            site = self.model.objects.filter(id=self.request.GET['id'])
            if site != None:
                siteHaveProduct = productOfSite(site)
                siteHaveScore = scoreOfSites(siteHaveProduct)
                result = keywordOfSites(siteHaveScore, 10)
                temp = []
                for res in result:
                    res.category = res.cat.chinese_name
                    temp.append(res)
                return list(temp)
        return

class searchSite(generics.ListAPIView):
    serializer_class = SearchSerializer
    model = serializer_class.Meta.model
    def get_queryset(self):
        if 'sitename' in self.request.GET and self.request.GET['sitename'] != "":
            sitename = self.request.GET['sitename']
            sites = self.model.objects.filter(isOpen=True)
            temp = []
            for site in sites:
                if site.name.find(sitename) != -1:
                    temp.append(site)
            return temp
        return
