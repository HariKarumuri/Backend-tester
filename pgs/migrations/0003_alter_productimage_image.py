# Generated by Django 4.2.1 on 2023-06-02 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgs', '0002_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.FileField(upload_to='products/'),
        ),
    ]
