# Generated by Django 4.2.1 on 2023-06-02 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgs', '0008_furnishing_securityamenity_services_topamenities_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='single_sharing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='single_sharing_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
