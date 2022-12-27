from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'

    def __str__(self):
        return self.name


class SubSubCategory(models.Model):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sub Sub Category'
        verbose_name_plural = 'Sub Sub Categories'

    def __unicode__(self):
        return f"{self.subcategory.category.name} -> {self.subcategory.name} -> {self.name}"

    def __str__(self):
        return self.name
