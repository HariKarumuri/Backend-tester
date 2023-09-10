from django.contrib import admin
from .models import SideAd ,BannerAd ,SkyScrapperAd ,PremiumAds ,PopularAds


class SideAdAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'duration_in_days', 'is_paid', 'is_show', 'priority')

class BannerAdAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'link', 'is_active')

class SkyScrapperAdAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'link', 'is_active')   


class PremiumAdsAdmin(admin.ModelAdmin):
    list_display = ('locality', 'is_active', 'product')
    list_filter = ('locality', 'is_active')
    search_fields = ('locality', 'product__name')  # Adjust fields as needed

class PopularAdsAdmin(admin.ModelAdmin):
    list_display = ('locality', 'is_active', 'selected_products')

    def selected_products(self, obj):
        return ', '.join([product.product_name for product in obj.products.all()])
    selected_products.short_description = 'Selected Products'





admin.site.register(PopularAds, PopularAdsAdmin)    
admin.site.register(PremiumAds, PremiumAdsAdmin)    
admin.site.register(SideAd, SideAdAdmin)
admin.site.register(BannerAd, BannerAdAdmin)
admin.site.register(SkyScrapperAd,SkyScrapperAdAdmin)



