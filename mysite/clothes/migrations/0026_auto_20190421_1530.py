# Generated by Django 2.1.7 on 2019-04-21 11:30

import clothes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0025_auto_20190421_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='/item_no_image.png', upload_to=clothes.models.image_folder, verbose_name='Изображение'),
        ),
    ]
