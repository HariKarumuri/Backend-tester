from django.urls import path
from ads_manager.views import SideAdListView , BannerAdListView , SkyScrapperAdListView , PremiumAdsListView ,PopularAdsListView
from pgs.views import  ProductListView , ProductDetailView 
from bookings.views import BookingView
from django.conf import settings # new
from  django.conf.urls.static import static #new



urlpatterns = [
    
    path('booking/', BookingView.as_view(), name='booking'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),   
    path('side_ads/', SideAdListView.as_view(), name='side_ads'),
    path('banner_ads/', BannerAdListView.as_view(), name='banner_ads'),
    path('sky_scrapper_ads/', SkyScrapperAdListView.as_view(), name='sky_scrapper_ads'),
    path('premium_ads/', PremiumAdsListView.as_view(), name='premium_ads'),
    path('popular_ads/', PopularAdsListView.as_view(), name='popular_ads'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)