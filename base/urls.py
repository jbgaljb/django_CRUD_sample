from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
]
