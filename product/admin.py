from django.contrib import admin
from .models import *


# Register your models here.


class FeatureInline(admin.TabularInline):
    model = ProductFeatures
    extra = 0


class ImageInline(admin.TabularInline):
    model = Images
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'inventory', 'price', 'offers', 'new_price', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [FeatureInline, ImageInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductFeatures)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'product']
