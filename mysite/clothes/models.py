from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    photo = models.FileField(upload_to='item_photo', null=True);
    #material
    cost = models.PositiveSmallIntegerField()
    #size
    #gender
    #category
    def __str__(self):
        return self.name
    
