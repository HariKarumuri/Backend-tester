from rest_framework import serializers
from .models import order , Product


class OrderSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = order
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    common_areas = serializers.StringRelatedField(many=True)
    security_amenities = serializers.StringRelatedField(many=True)
    furnishing_in_property = serializers.StringRelatedField(many=True)
    services_in_property = serializers.StringRelatedField(many=True)
    topAmenities_in_property = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = '__all__'