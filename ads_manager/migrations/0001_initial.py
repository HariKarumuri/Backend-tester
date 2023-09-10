# Generated by Django 4.2.1 on 2023-08-15 18:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pgs', '0032_product_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueLocalityAds23',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BTM_Layout', models.OneToOneField(default=None, help_text='Select an ad for BTM Layout (only one allowed).', limit_choices_to={'locality': 'BTM Layout'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='btm_layout_ad', to='pgs.product')),
                ('Bellandur_Layout', models.OneToOneField(default=None, limit_choices_to={'locality': 'Bellandur'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bellandur_layout_ad', to='pgs.product')),
                ('ElectronicCity_Layout', models.OneToOneField(default=None, limit_choices_to={'locality': 'Electronic City'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electronic_city_layout_ad', to='pgs.product')),
                ('HSR_Layout', models.OneToOneField(default=None, limit_choices_to={'locality': 'HSR Layout'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hsr_layout_ad', to='pgs.product')),
                ('Koramangala_Layout', models.OneToOneField(default=None, limit_choices_to={'locality': 'Koramangala'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='koramangala_layout_ad', to='pgs.product')),
                ('Madiwala_Layout', models.OneToOneField(default=None, limit_choices_to={'locality': 'Madiwala'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='madiwala_layout_ad', to='pgs.product')),
                ('ManyataTechPark_Layout', models.OneToOneField(default=None, limit_choices_to={'locality': 'Manyata Tech Park'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manyata_tech_park_layout_ad', to='pgs.product')),
                ('Marathalli_Layout', models.OneToOneField(default=None, limit_choices_to={'locality': 'Marathalli'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marathalli_layout_ad', to='pgs.product')),
                ('SarjapurRoad_Layout', models.OneToOneField(default=None, limit_choices_to={'locality': 'Sarjapur Road'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sarjapur_road_layout_ad', to='pgs.product')),
                ('Whitefield_Layout', models.OneToOneField(default=None, limit_choices_to={'locality': 'Whitefield'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whitefield_layout_ad', to='pgs.product')),
            ],
        ),
        migrations.CreateModel(
            name='SkyScrapperAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='skyscrapper_ads/')),
                ('is_active', models.BooleanField(default=True)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skyscrapper_ads', to='pgs.product')),
            ],
        ),
        migrations.CreateModel(
            name='SideAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration_in_days', models.PositiveIntegerField(default=30)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_show', models.BooleanField(default=True)),
                ('priority', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=2)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='side_ad', to='pgs.product')),
            ],
        ),
        migrations.CreateModel(
            name='BannerAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='banner_ads/')),
                ('is_active', models.BooleanField(default=True)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banner_ads', to='pgs.product')),
            ],
        ),
    ]