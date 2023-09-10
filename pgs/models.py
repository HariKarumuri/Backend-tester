from django.db import models
from PIL import Image
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

  

class Product(TimestampModel):
    PG_NAME_CHOICES = (
        ('girls', 'Girls'),
        ('boys', 'Boys'),
        ('coliving', 'Co-living'),
    )
    SUITED_FOR_CHOICES = (
        ('students', 'Students'),
        ('professionals', 'Professionals'),
        ('students & professionals', 'students & professionals'),
    )
    MANAGED_BY_CHOICES = (
        ('landlord', 'Landlord'),
        ('caretaker', 'Caretaker'),
        ('dedicated_professional', 'Dedicated Professional'),
    )
    LOCALITY_CHOICES = (
        ('Marathalli', 'Marathalli'),
        ('BTM Layout', 'BTM Layout'),
        ('Electronic City', 'Electronic City'),
        ('Manyata Tech Park', 'Manyata Tech Park'),
        ('Whitefield', 'Whitefield'),
        ('Sarjapur Road', 'Sarjapur Road'),
        ('Madiwala', 'Madiwala'),
        ('Koramangala', 'Koramangala'),
        ('HSR Layout', 'HSR Layout'),
        ('Bellandur', 'Bellandur'),
    )

    product_name = models.CharField(max_length=180)
    description = models.TextField(max_length=180)
    phone_number = PhoneNumberField(blank=False, null=False ,default="your_default_phone_number")
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_beds = models.PositiveIntegerField(default=0)
    single_sharing = models.BooleanField(default=False)
    single_sharing_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    single_sharing_deposite = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    double_sharing = models.BooleanField(default=False)
    double_sharing_deposite = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    double_sharing_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    triple_sharing = models.BooleanField(default=False)
    triple_sharing_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    triple_sharing_deposite = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    maintaince_charge = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    electric_charge = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pg_for = models.CharField(max_length=20, choices=PG_NAME_CHOICES,default='')
    best_suited_for = models.CharField(max_length=40, choices=SUITED_FOR_CHOICES , default='')
    meals_available = models.BooleanField(default=False)
    notice_period = models.PositiveIntegerField(default=0)
    lock_in_period = models.PositiveIntegerField(default=0)
    common_areas = models.ManyToManyField('CommonArea', related_name='products')
    property_managed_by = models.CharField(max_length=40, choices=MANAGED_BY_CHOICES, default='')
    property_manager_stays = models.BooleanField(default=False)
    security_amenities = models.ManyToManyField('SecurityAmenity',related_name='products' )
    furnishing_in_property = models.ManyToManyField('Furnishing',related_name='products' )
    services_in_property = models.ManyToManyField('Services',related_name='products' )
    topAmenities_in_property = models.ManyToManyField('TopAmenities',related_name='products' )
    city = models.CharField(max_length=180 , default='Banglore')
    locality = models.CharField(max_length=25,choices=LOCALITY_CHOICES,default='')
    embedded_map_src_link = models.CharField(max_length=100 , blank=True) 
    cover_image = models.FileField(upload_to='products/', null=True)  # Make image field nullable
    
    
    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name = "PG"
        verbose_name_plural = "PG"
    
class CommonArea(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    
    
    class Meta:
        verbose_name = "PG_CommonAreas"
        verbose_name_plural = "PG_CommonAreas"

class SecurityAmenity(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "PG_SecurityAmenity"
        verbose_name_plural = "PG_SecurityAmenity"

class Furnishing(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "PG_Furnitures"
        verbose_name_plural = "PG_Furnitures"

class Services(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "PG_Services"
        verbose_name_plural = "PG_Services"

class TopAmenities(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name        

    class Meta:
        verbose_name = "PG_TopAmenities"
        verbose_name_plural = "PG_TopAmenities"
 

class AdditionalImage(models.Model):
    MAX_IMAGES = 15

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to='more_images/')

    def clean(self):
        # Validate the number of additional images
        if AdditionalImage.objects.filter(product=self.product).count() >= self.MAX_IMAGES:
            raise ValidationError(f"Cannot add more than {self.MAX_IMAGES} additional images.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Run the clean() method before saving
        super().save(*args, **kwargs)

       

class AmenityImage(models.Model):
    MAX_IMAGES = 5

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='amenity_images')
    image = models.ImageField(upload_to='more_images/')

    def clean(self):
        # Validate the number of additional images
        if AdditionalImage.objects.filter(product=self.product).count() >= self.MAX_IMAGES:
            raise ValidationError(f"Cannot add more than {self.MAX_IMAGES} amenity images.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Run the clean() method before saving
        super().save(*args, **kwargs)     

class FoodImage(models.Model):
    MAX_IMAGES = 5

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Food_images')
    image = models.ImageField(upload_to='more_images/' , verbose_name="Only up to 5 images are supported.")

    def clean(self):
        # Validate the number of additional images
        if AdditionalImage.objects.filter(product=self.product).count() >= self.MAX_IMAGES:
            raise ValidationError(f"Cannot add more than {self.MAX_IMAGES} Food images.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Run the clean() method before saving
        super().save(*args, **kwargs)            
