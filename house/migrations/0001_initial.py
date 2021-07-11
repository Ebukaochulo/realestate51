# Generated by Django 3.2 on 2021-07-10 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField()),
                ('property_type', models.CharField(max_length=300)),
                ('rent', models.CharField(max_length=200)),
                ('baths', models.FloatField(default=0)),
                ('beds', models.FloatField(default=0)),
                ('garage', models.FloatField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(default='lagos', max_length=2000)),
                ('landing_page_view', models.ImageField(blank=True, null=True, upload_to='land/')),
                ('search_img', models.ImageField(blank=True, null=True, upload_to='land/')),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='picture/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='picture/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='picture/')),
            ],
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(max_length=300)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.house')),
            ],
        ),
    ]
