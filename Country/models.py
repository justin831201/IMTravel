from django.db import models

# Create your models here.
class Country(models.Model):
    chinese_name = models.CharField(max_length=20)
    english_name = models.CharField(max_length=30)
    def __str__(self):
        return self.chinese_name

class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    chinese_name = models.CharField(max_length=20)
    english_name = models.CharField(max_length=30)
    def __str__(self):
        return self.chinese_name
