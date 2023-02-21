from django.contrib import admin
from rest_framework.authtoken.models import Token

# Register your models here.
from products.models import Product


admin.site.register(Product)
