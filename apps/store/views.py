from django.shortcuts import render
from apps.categories.models import Category, SubCategory, SubSubCategory


def store(request):
    main_categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()
    sub_sub_categories = SubSubCategory.objects.all()
    context = {
        "main_categories": main_categories,
        'sub_categories': sub_categories,
        'sub_sub_categories': sub_sub_categories,
    }
    return render(request, 'store/main.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
