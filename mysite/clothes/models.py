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
    objects = ProductManager()

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)


def __str__(self):
    return "Cart item fro product {0}".format(self.item.name)


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)

    def add_to_cart(self, product_slug):
        cart = self
        product= Item.objects.get(slug=product_slug)
        new_item, _ = Item.objects.get_or_create(product=product, item_total=product.price)
        if new_item not in cart.items.all():
            cart.items.add(new_item)
            cart.save()


    def remove_from_cart(selfself, product_slug):
        cart = self
        product= Item.objects.get(slug=product_slug)
        for cart_item in cart.items.all():
            if cart_item.product == product:
                cart.items.remove(cart_item)
                cart.save()