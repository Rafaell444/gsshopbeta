from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name="cart"),
    path('product/<slug:slug>/', views.ProductDetail, name="product"),
    path('checkout/', views.checkout, name="checkout"),

]
