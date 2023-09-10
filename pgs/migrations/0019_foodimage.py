# Generated by Django 4.2.1 on 2023-06-27 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pgs', '0018_amenityimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='more_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Food_images', to='pgs.product')),
            ],
        ),
    ]
