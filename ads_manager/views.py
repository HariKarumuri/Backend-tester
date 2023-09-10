from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import SideAd ,BannerAd ,SkyScrapperAd ,PopularAds ,PremiumAds
from .serializers import SideAdSerializer , BannerAdSerializer , SkyScrapperAdSerializer ,PremiumAdsSerializer ,PopularAdsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class SideAdListView(generics.ListAPIView):
    queryset = SideAd.objects.all()
    serializer_class = SideAdSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['-priority']  # this will be how it should fetch in frontend
    ordering = ['-priority', '-created_at']  # Order by priority descending, then by created_at descending

class BannerAdListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            banner_ad = BannerAd.objects.get(is_active=True)
            serializer = BannerAdSerializer(banner_ad)
            return Response(serializer.data)
        except BannerAd.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class SkyScrapperAdListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            skyscrapper_ad = SkyScrapperAd.objects.get(is_active=True)
            serializer = SkyScrapperAdSerializer(skyscrapper_ad)
            return Response(serializer.data)
        except SkyScrapperAd.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PremiumAdsListView(generics.ListAPIView):
    queryset = PremiumAds.objects.all()
    serializer_class = PremiumAdsSerializer

class PopularAdsListView(generics.ListAPIView):
    queryset = PopularAds.objects.all()
    serializer_class = PopularAdsSerializer