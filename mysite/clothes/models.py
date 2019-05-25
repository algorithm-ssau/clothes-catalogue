from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)


class Item(models.Model):
    MATERIALS = (
        (None, ''),
        ('cotton', 'хлопок'),
        ('polyamide', 'полиамиды'),
        ('wool', 'шерсть'),
        ('polyester', 'полиэстеры'),
    )
    SIZES = (
        (None, ''),
        ('one', 'Один размер'),
        ('xs', 'XS'),
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL'),
        ('3xl', '3XL'),
    )
    GENDERS = (
        (None, ''),
        ('men', 'мужчинам'),
        ('women', 'женщинам'),
        ('unisex', 'unisex'),
        ('kids', 'детям'),
    )
    CATEGORIES = (
        (None, ''),
        ('shirts', 'рубашки'),
        ('coats', 'пальто и куртки'),
        ('sweatshirts', 'толстовки'),
        ('blouses', 'блузки'),
        ('pullovers', 'полуверы'),
        ('tshirts', 'футболки'),
        ('trousers', 'штаны'),
        ('shorts', 'шорты'),
        ('dresses', 'платья'),
        ('skirts', 'юбки'),
        ('accessories', 'аксессуары'),
        ('misc', 'разное'),

    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название')
    # slug is object URI address
    slug = models.SlugField(
        unique=True,
        default='',
        verbose_name='Идентификатор'
    )
    description = models.TextField(
        null=True,
        blank=True,
        max_length=600,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to=image_folder,
        default='/item_no_image.png',
        verbose_name='Изображение'
    )
    material = models.CharField(
        null=True,
        blank=True,
        max_length=10,
        choices=MATERIALS,
        default=None,
        verbose_name='Материал'
    )
    price = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=12,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name='Стоимость'
    )
    size = models.CharField(
        null=True,
        blank=True,
        max_length=11,
        choices=SIZES,
        default='m',
        verbose_name='Размер'
    )
    gender = models.CharField(
        null=True,
        blank=True,
        max_length=8,
        choices=GENDERS,
        default=None,
        verbose_name='Пол'
    )
    category = models.CharField(
        null=True,
        blank=True,
        max_length=15,
        choices=CATEGORIES,
        default=None,
        verbose_name='Категория'
    )
    available = models.BooleanField(
        default=True,
        verbose_name='В наличии'
    )

    def __str__(self):
        return self.name
