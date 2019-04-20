from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):

    MATERIALS = (
        ('cotton', 'хлопок'),
        ('polyamide', 'полиамиды'),
        ('wool', 'шерсть'),
        ('polyester', 'полиэстеры'),
    )
    SIZES = (
        ('one', 'один размер'),
        ('xs', 'XS'),
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL'),
        ('xxxl', 'XXXL'),
    )
    GENDERS = (
        ('men', 'мужчинам'),
        ('women', 'женщинам'),
        ('kids', 'детям'),
    )
    CATEGORIES = (
        ('shirts', 'рубашки'),
        ('coats', 'пальто и куртки'),
        ('sweatshirts', 'толстовки'),
        ('knitwear', 'трикотаж'),
        ('tshirts', 'футболки'),
        ('trousers', 'штаны'),
        ('shorts', 'шорты'),
        ('accessories', 'аксессуары'),
    )
    name = models.CharField(max_length=100, verbose_name='Название')
    # slug is object URI address
    slug = models.SlugField(
        unique=True,
        default='',
        verbose_name='Идентификатор'
    )
    description = models.TextField(
        null=True,
        verbose_name='Описание'
    )
    photo = models.FileField(
        upload_to='item_photo',
        null=True,
        verbose_name='Изображение'
    )
    material = models.CharField(
        max_length=10,
        choices=MATERIALS,
        default='cotton',
        verbose_name='Материал'
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name='Стоимость'
    )
    size = models.CharField(
        max_length=11,
        choices=SIZES,
        default='xs',
        verbose_name='Размер'
    )
    gender = models.CharField(
        max_length=8,
        choices=GENDERS,
        default='men',
        verbose_name='Пол'
    )
    category = models.CharField(
        max_length=15,
        choices=CATEGORIES,
        default='shirts',
        verbose_name='Категория'
    )
    available = models.BooleanField(
        default=True,
        verbose_name='В наличии'
    )

    def __str__(self):
        return self.name


