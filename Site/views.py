from django.shortcuts import render_to_response
from Country.models import Country, Region
from Site.models import Site, SiteView

# Create your views here.
def site(request):
    if 'site' in request.GET and request.GET['site'] != '':
        site = Site.objects.get(id=request.GET['site'])
        siteViews = SiteView.objects.filter(site=site)
    return render_to_response('site.html', locals())

