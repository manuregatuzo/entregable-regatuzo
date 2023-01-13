from django.db import models

class Order(models.Model):
    client = models.CharField(max_length=100)
    product = models.CharField(max_length=100)    
    payment_method = models.CharField(max_length=4)
    

