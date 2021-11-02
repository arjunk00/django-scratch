from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Users(AbstractUser):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    username = models.TextField(max_length=20, blank=False)
    password = models.TextField(blank=False)
    phone_no = models.IntegerField(blank=False)
    email = models.Charfield(blank=False)
    address = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=2, blank=False)
    age = models.IntegerField(blank=False)

class Catalog(models.model):
    product_id = models.TextField(primary_key=True,max_length=10, blank=False)
    product_name = models.CharField(blank=False)
    product_price = models.IntegerField(blank=False)
    product_desc = models.TextField(blank=False)

class Cart(models.model):
    product_instance = models.ForeignKey(Catalog)
    quantity = models.IntegerField(blank=False)
