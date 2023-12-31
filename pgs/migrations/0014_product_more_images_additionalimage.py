# Generated by Django 4.2.1 on 2023-06-22 17:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pgs', '0013_alter_productimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='more_images',
            field=models.FileField(blank=True, null=True, upload_to='more_images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])]),
        ),
        migrations.CreateModel(
            name='AdditionalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='more_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_images', to='pgs.product')),
            ],
        ),
    ]
