# Generated by Django 2.2 on 2019-04-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0005_auto_20190417_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.FilePathField(null=True),
        ),
    ]
