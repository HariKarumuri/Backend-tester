# Generated by Django 4.2.1 on 2023-08-01 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pgs', '0030_alter_commonarea_options_alter_furnishing_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'PG_Category', 'verbose_name_plural': 'PG_Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'PG', 'verbose_name_plural': 'PG'},
        ),
    ]