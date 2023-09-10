from django.shortcuts import render
from .models import Bookings ,Product
from .serializers import BookingsSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from django.core.mail import send_mail
from Popularpg.settings import EMAIL_HOST_USER

# Create your views here.
class BookingView(APIView):
    def get(self, request):
        try:
            bookings = Bookings.objects.all()
            serializer = BookingsSerializer(bookings, many=True)

            return Response({
                'data': serializer.data,
                'message': "Booking Data fetched Successfully"
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': "Something went wrong while fetching the data"
            }, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            serializer = BookingsSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': "Validation error occurred"
                }, status=status.HTTP_400_BAD_REQUEST)

            product_id = data.get('product')
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({
                    'data': {},
                    'message': f"Product with id {product_id} does not exist"
                }, status=status.HTTP_404_NOT_FOUND)

            subject = "New Booking is Initiated"
            message = f"Dear Customer {data['customer_name']},\n" \
                f"Your Booking has been initiated now for the following PG:\n\n" \
                f"PG Name: {product.product_name}\n" \
                f"Description: {product.description}\n" \
                f"Image: {product.cover_image.url}\n"
        
            email = data['customer_email']
            recipient_list = [email]
            send_mail(subject, message, EMAIL_HOST_USER, recipient_list, fail_silently=True)
            serializer.save()

            return Response({
                'data': serializer.data,
                'message': "New booking is created or placed"
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                'data': {},
                'message': f"Error occurred in creation of Booking: {str(e)}"
            }, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request):
        try:
            data = request.data
            booking = Bookings.objects.filter(id=data.get('id'))

            if not booking.exists():
                return Response({
                    'data': {},
                    'message': "Booking is not found with this ID"
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = BookingsSerializer(booking[0], data=data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': "Something went wrong"
                }, status=status.HTTP_500_BAD_REQUEST)

            serializer.save()

            return Response({
                'data': serializer.data,
                'message': "Booking is updated successfully"
             }, status=status.HTTP_200_OK)

        except:     
            return Response({
                'data': {},
                'message': "Something went wrong in updating the Booking"
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            data = request.data
            booking = Bookings.objects.filter(id=data.get('id'))
            
            if not booking.exists():
                return Response({
                    'data': {},
                    'message': "Booking is not found with this ID"
                }, status=status.HTTP_404_NOT_FOUND)

            booking[0].delete() 
            return Response({
                'data': {},
                'message': "Booking is deleted"
             }, status=status.HTTP_200_OK)

        except:  
            return Response({
                'data': {},
                'message': "Something went wrong in deleting the Booking"
            }, status=status.HTTP_400_BAD_REQUEST)
