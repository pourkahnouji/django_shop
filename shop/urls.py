from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('products/', views.products_list, name='product-list'),
    path('products/<slug:category_slug>/', views.products_list, name='product_list_by_category'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
