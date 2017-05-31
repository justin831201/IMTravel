from django.shortcuts import render_to_response
from Country.models import Country, Region
from Site.models import Site

# Create your views here.
def country(request):
    if 'country' in request.GET and request.GET['country'] != '':
        countryCandidate = Country.objects.get(chinese_name=request.GET['country'])
        regions = Region.objects.filter(country=countryCandidate)

    return render_to_response('country.html', locals())

def region(request):
    if 'country' in request.GET and request.GET['country'] != '' and 'region' in request.GET and request.GET['region'] != '':
        countryCandidate = Country.objects.get(chinese_name=request.GET['country'])
        regions = Region.objects.filter(country=countryCandidate)
        regionCandidate = regions.get(chinese_name=request.GET['region'])
        sites = Site.objects.filter(region=regionCandidate, isOpen=True)

    return render_to_response('region.html', locals())
