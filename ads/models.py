# ads/models.py
from django.db import models

class Ad(models.Model):
    ad_name = models.CharField(max_length=25 ,default='')
    ad_image = models.ImageField(upload_to='ads/',default=None)
    
    
    
