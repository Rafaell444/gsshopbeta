from django.urls import path

from apps.store.views import (SubSubCategoryProductView,
                              Store,
                              shop,
                              ProductDetail,
                              MainCategoryView,
                              SubCategoryView,
                              SubSubCategoryView)

urlpatterns = [
    path('product/<slug:slug>/', ProductDetail, name="product"),
    path('shop/', shop, name="checkout"),
    path('', Store.as_view(), name="main"),
    path('products/<str:name>/', SubSubCategoryProductView.as_view(), name="product_by_category"),
    path('main_categories/', MainCategoryView.as_view(), name="main_categories"),
    path('sub_categories/<str:name>/', SubCategoryView.as_view(), name="sub_categories"),
    path('sub_sub_categories/<str:name>/', SubSubCategoryView.as_view(), name="sub_sub_categories"),

]
