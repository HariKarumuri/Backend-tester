# Generated by Django 4.2.1 on 2023-06-02 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pgs', '0010_product_city_product_double_sharing_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='min_price',
        ),
    ]