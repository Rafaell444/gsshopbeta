from django.shortcuts import render, redirect
from django.views import View

from apps.categories.models import Category, SubCategory, SubSubCategory
from apps.products.models import Product, Picture


class Store(View):
    def get(self, request, *args, **kwargs):
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
    products = Product.objects.filter(slug=slug)
    product = products.filter(slug=slug).first()
    images = Picture.objects.filter(images__product_name=product.product_name)
    context = {
        "products": products,
        'images': images
    }

    return render(request, "store/single_product.html", context)


class SubSubCategoryProductView(View):
    def get(self, request, *args, **kwargs):
        category_name = self.kwargs['name']
        category = SubSubCategory.objects.filter(name=category_name).first()
        if category is None:
            return redirect('main')
        products_by_category = Product.objects.filter(category_id=category.id)
        context = {
            'products_by_category': products_by_category,
            'category': category,
        }
        return render(request, 'store/products_by_category.html', context)


class MainCategoryView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'store/categories/main_categories_list.html', context)


class SubCategoryView(View):
    def get(self, request, *args, **kwargs):
        category_name = self.kwargs['name']
        sub_categories = SubCategory.objects.filter(category__name=category_name)
        context = {
            'sub_categories': sub_categories
        }
        return render(request, 'store/categories/sub_categories_list.html', context)


class SubSubCategoryView(View):
    def get(self, request, *args, **kwargs):
        category_name = self.kwargs['name']
        sub_sub_categories = SubSubCategory.objects.filter(subcategory__name=category_name)
        context = {
            'sub_sub_categories': sub_sub_categories
        }
        return render(request, 'store/categories/sub_sub_categories.html', context)
