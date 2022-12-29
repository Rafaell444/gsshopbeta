from django.db import models
from apps.categories.models import SubSubCategory


class Product(models.Model):
    product_name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, blank=False)
    product_description = models.TextField(max_length=512)
    product_image = models.ImageField(upload_to='product_images', blank=True, null=True)
    category = models.ForeignKey(SubSubCategory, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    sale_percentage = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0)
    sale_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        if self.sale_percentage > 0:
            self.sale_price = self.price - (self.price * (self.sale_percentage / 100))
        else:
            self.sale_price = None
        super(Product, self).save(*args, **kwargs)
