# Generated by Django 5.2.4 on 2025-07-20 11:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_itemcategory_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
