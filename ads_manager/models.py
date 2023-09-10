from django.db import models 
from django import forms
from django.db import models
from pgs.models import Product  # Import the Product model from the pg app
from django.utils import timezone
from django.core.exceptions import ValidationError

class SideAd(models.Model):
    PRIORITY_CHOICES = (
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    )
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='side_ad', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    duration_in_days = models.PositiveIntegerField(default=30)  # Change the default value as needed
    is_paid = models.BooleanField(default=False)
    is_show = models.BooleanField(default=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)  # Default to Medium

    def __str__(self):
        return self.name

    def update_is_show(self):
        # Calculate the date after the specified duration
        expiration_date = self.created_at + timezone.timedelta(days=self.duration_in_days)
        
        # Compare with the current date
        if timezone.now() > expiration_date:
            self.is_show = False
            self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_is_show()

class BannerAd(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banner_ads/')
    link = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='banner_ads')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_active:
            # Deactivate all other active banner ads
            BannerAd.objects.exclude(pk=self.pk).update(is_active=False)
        
        super().save(*args, **kwargs)   

class SkyScrapperAd(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='skyscrapper_ads/')
    link = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='skyscrapper_ads')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_active:
            # Deactivate all other active skyscrapper ads
            SkyScrapperAd.objects.exclude(pk=self.pk).update(is_active=False)
        
        super().save(*args, **kwargs)             



class PremiumAds(models.Model):
    locality = models.CharField(
        max_length=100,  # Adjust the max length as needed
        choices=Product.LOCALITY_CHOICES,  # Assuming LOCALITY_CHOICES is a choice field in your Product model
        unique=True
    )
    is_active = models.BooleanField(default=False)
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='premium_ad'
    )

    def save(self, *args, **kwargs):
        if self.is_active:
            PremiumAds.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Premium Ad for {self.locality}"


class PopularAds(models.Model):
    locality = models.CharField(max_length=100, choices=Product.LOCALITY_CHOICES)
    is_active = models.BooleanField(default=False)
    products = models.ManyToManyField(Product, related_name='popular_ads')

    def save(self, *args, **kwargs):
        if self.is_active:
            PopularAds.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Popular Ad for {self.locality}"