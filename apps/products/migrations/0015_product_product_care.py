# Generated by Django 4.1.4 on 2022-12-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_rename_product_main_description_product_product_specifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_care',
            field=models.TextField(default=1, max_length=512),
            preserve_default=False,
        ),
    ]