from django.db import models
from apps.categories.models import SubSubCategory


class Product(models.Model):
    product_name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    product_description = models.TextField(max_length=512)
    category = models.ForeignKey(SubSubCategory, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product_name


