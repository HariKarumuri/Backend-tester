from django.shortcuts import render

from .models import  Product 
from .serializers import  ProductSerializer , AdditionalImage

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import JsonResponse

# Create your views here.

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serialized_products = [ProductSerializer(product).data for product in products]
        return JsonResponse(serialized_products, safe=False)

class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return JsonResponse(serializer.data)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


