from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.fields.related import ForeignKey


# Create your models here.


class Users(AbstractUser):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    username = models.TextField(max_length=20, unique=True, blank=False)
    password = models.TextField(blank=False)
    phone_no = models.IntegerField(null=True)
    email = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=2, blank=False)
    age = models.IntegerField(blank=False, null=True)


class Catalog(models.Model):
    product_id = models.TextField(primary_key=True, max_length=10, blank=False)
    product_name = models.CharField(max_length=20, blank=False)
    product_price = models.IntegerField(blank=False)
    product_desc = models.TextField(blank=False)


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    ordered = models.BooleanField(default=False)
    product_instance = models.ForeignKey(Catalog, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.quantity} of {self.product_instance.product_name}"

    def get_total_item_price(self):
        return self.quantity * self.product_instance.product_price

    def get_final_price(self):
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    items = models.ManyToManyField(Cart)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def total_price(self):
        total=0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
