from import_export import resources
from import_export.admin import TabularInline
from .models import Product  # Import your model

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product  # Use your model
