# Generated by Django 2.0.7 on 2018-09-19 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('listing_type', models.TextField(max_length=255)),
                ('guests', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('city', models.TextField(blank=True, max_length=255)),
                ('state', models.TextField(blank=True, max_length=255)),
                ('price', models.IntegerField(null=True)),
                ('rating', models.IntegerField(null=True)),
                ('main_photo', models.ImageField(default='unkownListing.png', upload_to='media')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amenities', models.ManyToManyField(related_name='listing_group', to='listing.Amenity')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='noProfile.png', upload_to='media')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='listing.Listing')),
            ],
        ),
    ]
