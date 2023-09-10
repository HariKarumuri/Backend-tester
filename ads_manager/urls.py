from django.urls import path
from .views import SideAdListView

urlpatterns = [
    # Other URL patterns
    path('side-ads/', SideAdListView.as_view(), name='side-ads-list'),
]
