# Generated by Django 4.2.1 on 2023-08-15 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgs', '0034_delete_category'),
        ('ads_manager', '0005_popularads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularads',
            name='products',
            field=models.ManyToManyField(limit_choices_to={'is_active': True}, related_name='popular_ads', to='pgs.product'),
        ),
    ]
