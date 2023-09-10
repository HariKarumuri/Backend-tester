# Generated by Django 4.2.1 on 2023-07-27 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerBlissAd',
            fields=[
                ('ad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ads.ad')),
            ],
            bases=('ads.ad',),
        ),
        migrations.CreateModel(
            name='CozyCornersAd',
            fields=[
                ('ad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ads.ad')),
            ],
            bases=('ads.ad',),
        ),
        migrations.CreateModel(
            name='ExclusiveOffersAd',
            fields=[
                ('ad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ads.ad')),
            ],
            bases=('ads.ad',),
        ),
        migrations.CreateModel(
            name='FeaturedGemsAd',
            fields=[
                ('ad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ads.ad')),
            ],
            bases=('ads.ad',),
        ),
        migrations.CreateModel(
            name='HeroSpotlightAd',
            fields=[
                ('ad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ads.ad')),
            ],
            bases=('ads.ad',),
        ),
        migrations.CreateModel(
            name='TopPicksAd',
            fields=[
                ('ad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ads.ad')),
            ],
            bases=('ads.ad',),
        ),
    ]