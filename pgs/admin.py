from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import  Product, CommonArea, Services, TopAmenities, SecurityAmenity, Furnishing, AdditionalImage, AmenityImage, FoodImage
from import_export import resources

class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage

class AmenityImageInline(admin.TabularInline):
    model = AmenityImage

class FoodImageInline(admin.TabularInline):
    model = FoodImage

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = (
            'id',
            'product_name', 'description', 'phone_number', 'min_price', 'total_beds', 'single_sharing' , 'single_sharing_price' , 'single_sharing_deposite', 
            'double_sharing',
            'double_sharing_deposite',
            'double_sharing_price',
            'triple_sharing',
            'triple_sharing_price',
            'triple_sharing_deposite',
            'maintaince_charge',
            'electric_charge',
            'pg_for',
            'best_suited_for',
            'meals_available',
            'notice_period',
            'lock_in_period',
            'common_areas',
            'property_managed_by',
            'property_manager_stays',
            'security_amenities',
            'furnishing_in_property',
            'services_in_property',
            'topAmenities_in_property',
            'city',
            'locality',
            'embedded_map_src_link',
            'cover_image'



           
        )



class ProductInline(admin.TabularInline):
    model = Product
    resource_class = ProductResource

@admin.register(Product)
class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['product_name', 'min_price', 'single_sharing', 'double_sharing', 'triple_sharing', 'locality', 'updated_at', 'phone_number']
    list_filter = ['single_sharing', 'double_sharing', 'triple_sharing', 'locality']
    inlines = [AdditionalImageInline, AmenityImageInline, FoodImageInline]
    resource_class = ProductResource

@admin.register(CommonArea)
class CommonAreaAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(SecurityAmenity)
class SecurityAmenityAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Furnishing)
class FurnishingAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(TopAmenities)
class TopAmenitiesAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name']
