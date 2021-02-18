from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    product_name = models.CharField(max_length=30,unique=True)
    price = models.FloatField(validators=[MinValueValidator(1)],default = 0)

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    name = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.FloatField(validators=[MinValueValidator(1)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='admin')
