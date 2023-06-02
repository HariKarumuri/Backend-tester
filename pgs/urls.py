from django.urls import path
from pgs.views import OrderView , ProductListView , ProductDetailView

urlpatterns = [
    
    path('order/', OrderView.as_view(), name='order'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
