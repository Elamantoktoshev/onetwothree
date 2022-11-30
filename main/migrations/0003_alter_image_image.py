# Generated by Django 4.1.3 on 2022-11-30 16:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_advert_whatsapp_number_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='https://res.cloudinary.com/drw2jobkz/images'),
        ),
    ]
