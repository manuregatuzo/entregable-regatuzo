from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='productsimg', null=True, blank=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)