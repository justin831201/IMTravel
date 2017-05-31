from django.db import models
#from Site.models import Site

# Create your models here.
class Category(models.Model):
    chinese_name = models.CharField(max_length=10)
#    english_name = models.CharField(max_length=20)
    def __str__(self):
        return self.chinese_name

#class Tag(models.Model):
#    category = models.ForeignKey(Category, on_delete=models.CASCADE)
#    site = models.ForeignKey(Site, on_delete=models.CASCADE)
#    def __str__(self):
#        return self.category.chinese_name + '-' + self.site.name
