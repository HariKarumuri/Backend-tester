from django.db import models



# Create your models here.

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimestampModel):
    category_name = models.CharField(max_length=180)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.category_name

class Product(TimestampModel):
    PG_NAME_CHOICES = (
        ('girls', 'Girls'),
        ('boys', 'Boys'),
        ('coliving', 'Co-living'),
    )
    SUITED_FOR_CHOICES = (
        ('students', 'Students'),
        ('professionals', 'Professionals'),
    )
    MANAGED_BY_CHOICES = (
        ('landlord', 'Landlord'),
        ('caretaker', 'Caretaker'),
        ('dedicated_professional', 'Dedicated Professional'),
    )
    product_name = models.CharField(max_length=180)
    description = models.TextField(max_length=180)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to='products/', null=True)  # Make image field nullable
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    pg_name = models.CharField(max_length=180, blank=True)
    total_beds = models.PositiveIntegerField(default=0)
    single_sharing = models.BooleanField(default=False)
    single_sharing_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    double_sharing = models.BooleanField(default=False)
    double_sharing_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    triple_sharing = models.BooleanField(default=False)
    triple_sharing_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    security_deposite = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True )
    pg_for = models.CharField(max_length=20, choices=PG_NAME_CHOICES,default='')
    best_suited_for = models.CharField(max_length=20, choices=SUITED_FOR_CHOICES , default='')
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
    locality = models.CharField(max_length=300,blank=True)
    
    
    def __str__(self):
        return self.product_name
    
class CommonArea(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    
    

class SecurityAmenity(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Furnishing(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Services(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TopAmenities(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name        

class order(TimestampModel):
    customer_name = models.CharField(max_length=180)
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "Order #1"

