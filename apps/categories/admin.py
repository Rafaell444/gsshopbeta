from django.contrib import admin
from apps.categories.models import Category, SubCategory, SubSubCategory

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SubSubCategory)
