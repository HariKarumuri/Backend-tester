# Generated by Django 4.2.1 on 2023-06-27 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pgs', '0020_rename_image_product_cover_image_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
