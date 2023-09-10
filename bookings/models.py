from django.db import models
from pgs.models import Product , TimestampModel

class Bookings(TimestampModel):
    customer_name = models.CharField(max_length=180)
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_phone = models.CharField(max_length=15, blank=True, null=True)  # Add phone number field
    

    def __str__(self):
        return "Booking #1"

