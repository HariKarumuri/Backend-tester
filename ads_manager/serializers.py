from rest_framework import serializers
from .models import SideAd , BannerAd, SkyScrapperAd  ,PopularAds,PremiumAds
from pgs.serializers import ProductSerializer 



class SideAdSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = SideAd
        fields = '__all__'

class BannerAdSerializer(serializers.ModelSerializer):
    product = ProductSerializer(source='link')

    class Meta:
        model = BannerAd
        fields = '__all__'

class SkyScrapperAdSerializer(serializers.ModelSerializer):
    product = ProductSerializer(source='link')

    class Meta:
        model = SkyScrapperAd
        fields = '__all__'        

class PopularAdsSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = PopularAds
        fields = '__all__'

class PremiumAdsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = PremiumAds
        fields = '__all__'
