from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Appetizer(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    stock = models.IntegerField()
    image_url = models.URLField(max_length=2080)

    def __str__(self):
        return f"{self.name}"
    
    
class Entree(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    stock = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.URLField(max_length=2080)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    appetizers = models.ManyToManyField('Appetizer', related_name='carts')

    def __str__(self):
        return f"Cart for {self.user.username}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appetizers = models.ManyToManyField('Appetizer', related_name='orders')
    # Add more fields as needed, such as total_price, timestamp, etc.
    
    def __str__(self):
        return f"Order for {self.user.username}"
    