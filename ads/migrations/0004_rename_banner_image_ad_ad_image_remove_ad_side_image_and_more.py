# Generated by Django 4.2.1 on 2023-08-01 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_remove_cozycornersad_ad_ptr_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='banner_image',
            new_name='ad_image',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='side_image',
        ),
        migrations.AddField(
            model_name='ad',
            name='ad_name',
            field=models.CharField(default='', max_length=25),
        ),
    ]
