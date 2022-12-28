# Generated by Django 4.1.4 on 2022-12-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_sale_percentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7),
        ),
    ]