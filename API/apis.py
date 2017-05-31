from rest_framework import serializers
from Site.models import Site

#class SiteSerializer(serializers.HyperlinkedModelSerializer):
class SiteSerializer(serializers.ModelSerializer):
    keywords = serializers.CharField(read_only=True)
    category = serializers.CharField(read_only=True)
    girlScore = serializers.IntegerField(read_only=True)
    boyScore = serializers.IntegerField(read_only=True)
    classmateScore = serializers.IntegerField(read_only=True)
    coupleScore = serializers.IntegerField(read_only=True)
    childrenScore = serializers.IntegerField(read_only=True)
    familyScore = serializers.IntegerField(read_only=True)
    score = serializers.IntegerField(read_only=True)
    time = serializers.IntegerField(read_only=True)
    productNumber = serializers.IntegerField(read_only=True)
    productName = serializers.ListField(
        child = serializers.CharField(read_only=True)
    )
    productPrice = serializers.ListField(
        child = serializers.IntegerField(read_only=True)
    )
    productEachNumber = serializers.ListField(
        child = serializers.IntegerField(read_only=True)
    )
    class Meta:
        model = Site
        fields = '__all__'

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ('id', 'name')
