from rest_framework import serializers
from .models import  Product ,AdditionalImage , AmenityImage , FoodImage




class AdditionalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalImage
        fields = ['id', 'image']      
class AmenityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenityImage
        fields = ['id', 'image']      

class FoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodImage
        fields = ['id', 'image'] 

class ProductSerializer(serializers.ModelSerializer):
    common_areas = serializers.StringRelatedField(many=True)
    security_amenities = serializers.StringRelatedField(many=True)
    furnishing_in_property = serializers.StringRelatedField(many=True)
    services_in_property = serializers.StringRelatedField(many=True)
    topAmenities_in_property = serializers.StringRelatedField(many=True)
    additional_images = AdditionalImageSerializer(many=True)  # Include the additional images field
    amenity_images = AmenityImageSerializer(many=True)  # Include the additional images field
    Food_images = FoodImageSerializer(many=True)  # Include the additional images field


    class Meta:
        model = Product
        fields = '__all__'