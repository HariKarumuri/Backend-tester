# Generated by Django 4.2.1 on 2023-08-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_rename_banner_image_ad_ad_image_remove_ad_side_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='link',
            field=models.URLField(blank=True, default=None),
        ),
    ]
