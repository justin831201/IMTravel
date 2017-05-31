from django.db import models
from Country.models import Region
from Category.models import Category

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=50)
    longitude = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
    latitude = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default='')
    info = models.CharField(max_length=2000, default='')
    transportation = models.CharField(max_length=1500, default='', blank=True)
    openTime = models.CharField(max_length=500, default='', blank=True)
    isOpen = models.BooleanField(default=True)
    #category = models.CharField(max_length=20, default='', blank=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    #boyAsset = models.IntegerField(default=0, blank=True)
    #girlAsset = models.IntegerField(default=0, blank=True)
    #classmateAsset = models.IntegerField(default=0, blank=True)
    #coupleAsset = models.IntegerField(default=0, blank=True)
    #familyAsset = models.IntegerField(default=0, blank=True)
    #childrenAsset = models.IntegerField(default=0, blank=True)
    def __str__(self):
        return str(self.id) + '-' + self.name

class Keyword(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    description = models.CharField(max_length=20)
    def __str__(self):
        return self.description

class SiteView(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    location = models.CharField(max_length=1000, default='')
    def __str__(self):
        return self.site.name + '-' + self.location
