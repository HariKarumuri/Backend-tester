# Generated by Django 4.2.1 on 2023-06-28 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgs', '0025_alter_foodimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodimage',
            name='image',
            field=models.ImageField(upload_to='more_images/', verbose_name='Only up to 5 images are supported.'),
        ),
    ]