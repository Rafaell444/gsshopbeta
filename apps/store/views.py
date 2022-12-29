from django.shortcuts import render
from django.views import View

from apps.categories.models import Category, SubCategory, SubSubCategory
from apps.products.models import Product


def store(request):
    main_categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()
    sub_sub_categories = SubSubCategory.objects.all()
    products = Product.objects.all()
    context = {
        "main_categories": main_categories,
        'sub_categories': sub_categories,
        'sub_sub_categories': sub_sub_categories,
        'products': products
    }
    return render(request, 'store/main_content.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def ProductDetail(request, slug):
    product = Product.objects.get(slug=slug)

    context = {
        "product": product
    }

    return render(request, "store/single_product.html", context)
