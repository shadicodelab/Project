from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Appetizer(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    stock = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.URLField(max_length=2080)
    
    
class Entree(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    stock = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.URLField(max_length=2080)
