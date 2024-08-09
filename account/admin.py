from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(ShopUser)
class ShopUserAdmin(admin.ModelAdmin):
    ordering = ['phone']
    list_display = ['phone', 'first_name', 'last_name', 'is_staff', 'is_superuser']
