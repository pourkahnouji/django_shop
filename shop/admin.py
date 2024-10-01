from django.contrib import admin
from .models import *


# Register your models here.

class FeaturesInline(admin.TabularInline):
    model = ProductFeature
    extra = 0


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'inventory', 'price', 'discount', 'new_price']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [FeaturesInline, ImageInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
