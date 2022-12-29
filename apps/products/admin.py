from django.contrib import admin

from apps.products.models import Product, Picture

admin.site.register(Product)
admin.site.register(Picture)
