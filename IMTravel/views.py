from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from Site.models import Site
from Country.models import Region
from pymongo import MongoClient
from Site.function import keywordOfSites, scoreOfSites

def index(request):
    taipei = Region.objects.get(chinese_name="台北")
    oldSites = Site.objects.filter(region=taipei, isOpen=True)
    sitesHaveScore = scoreOfSites(oldSites)
    sites = keywordOfSites(sitesHaveScore, 5)
    return render_to_response('index.html', locals())

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/');
    else:
        form = UserCreationForm()
        return render_to_response('registration/register.html', RequestContext(request, locals()))
