from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class ProductManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)

def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)

class Item(models.Model):
    MATERIALS = (
        (None, 'прочее'),
        ('cotton', 'хлопок'),
        ('polyamide', 'полиамиды'),
        ('wool', 'шерсть'),
        ('polyester', 'полиэстеры'),
        ('silk', 'шелк'),
        ('velveteen', 'вельвет'),
        ('viscose', 'вискоза'),
        ('satin', 'сатин'),
    )

    SIZES = (
        (None, 'один размер'),
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
        ('unisex', 'унисекс'),
        ('kids', 'детям'),
    )

    CATEGORIES = (
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
    )

    name = models.CharField(
        max_length=100,
        verbose_name='название')

    slug = models.SlugField(
        unique=True,
        default='',
        verbose_name='идентификатор'
    )

    description = models.TextField(
        null=True,
        blank=True,
        max_length=600,
        verbose_name='описание'
    )

    image = models.ImageField(
        upload_to=image_folder,
        default='/item_no_image.png',
        verbose_name='изображение'
    )

    material = models.CharField(
        null=True,
        blank=True,
        max_length=10,
        choices=MATERIALS,
        default=None,
        verbose_name='материал'
    )

    price = models.DecimalField(
        decimal_places=0,
        max_digits=12,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name='стоимость'
    )

    size = models.CharField(
        null=True,
        blank=True,
        max_length=11,
        choices=SIZES,
        default='m',
        verbose_name='размер'
    )

    gender = models.CharField(
        null=True,
        blank=True,
        max_length=8,
        choices=GENDERS,
        default=None,
        verbose_name='пол'
    )

    category = models.CharField(
        null=True,
        blank=True,
        max_length=15,
        choices=CATEGORIES,
        default=None,
        verbose_name='категория'
    )

    available = models.BooleanField(
        default=True,
        verbose_name='в наличии'
    )

    objects = ProductManager()

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        super(Item, self).delete(*args, **kwargs)