from django.contrib import admin
from django.forms import inlineformset_factory
from .models import Bookings

# Register your models here.

@admin.register(Bookings)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name','customer_email', 'product','created_at', 'updated_at']