# Generated by Django 4.2.1 on 2023-08-01 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pgs', '0029_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commonarea',
            options={'verbose_name': 'PG_CommonAreas', 'verbose_name_plural': 'PG_CommonAreas'},
        ),
        migrations.AlterModelOptions(
            name='furnishing',
            options={'verbose_name': 'PG_Furnitures', 'verbose_name_plural': 'PG_Furnitures'},
        ),
        migrations.AlterModelOptions(
            name='securityamenity',
            options={'verbose_name': 'PG_SecurityAmenity', 'verbose_name_plural': 'PG_SecurityAmenity'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'PG_Services', 'verbose_name_plural': 'PG_Services'},
        ),
        migrations.AlterModelOptions(
            name='topamenities',
            options={'verbose_name': 'PG_TopAmenities', 'verbose_name_plural': 'PG_TopAmenities'},
        ),
    ]