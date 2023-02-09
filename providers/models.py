from django.db import models

# Create your models here.
class Providers(models.Model):
    CONDITION_CHOICES = (
        ('monotributista', 'monotribustista'),
        ('responsable inscripto','responsable inscripto'),
    )

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    condition = models.CharField(max_length=50, choices = CONDITION_CHOICES)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='productsimg', null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.email}'