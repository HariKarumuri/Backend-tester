from django.urls import path
from pgs.views import OrderView , ProductListView , ProductDetailView
from django.conf import settings # new
from  django.conf.urls.static import static #new

urlpatterns = [
    
    path('order/', OrderView.as_view(), name='order'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)