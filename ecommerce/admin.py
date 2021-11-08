from django.contrib import admin
from .models import Users, Catalog, Cart

# Register your models here.

admin.site.register(Users)
admin.site.register(Catalog)
admin.site.register(Cart)