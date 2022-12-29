from django.urls import path

from apps.store.views import SubSubCategoryProductView, store, checkout, ProductDetail

urlpatterns = [
    path('product/<slug:slug>/', ProductDetail, name="product"),
    path('checkout/', checkout, name="checkout"),
    path('', store, name="main"),
    path('products/<str:name>/', SubSubCategoryProductView.as_view(), name="product_by_category"),

]
