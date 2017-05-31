from django.contrib import admin
from Site.models import Site, Keyword, SiteView

# Register your models here.
admin.site.register(Site)
admin.site.register(Keyword)
admin.site.register(SiteView)
