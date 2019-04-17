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
        ('trousers', 'щтаны'),
        ('shorts', 'шорты'),
        ('accessories', 'аксессуары'),
    )
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    photo = models.FileField(upload_to='item_photo', null=True);
    material = models.CharField(
        max_length=10,
        choices=MATERIALS,
        default='cotton'
    )
    cost = models.PositiveSmallIntegerField()
    size = models.CharField(
        max_length=11,
        choices=SIZES,
        default='xs'
    )
    gender = models.CharField(
        max_length=8,
        choices=GENDERS,
        default='men'
    )
    category = models.CharField(
        max_length=15,
        choices=CATEGORIES,
        default='shirts'
    )
    def __str__(self):
        return self.name
    
