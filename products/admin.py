from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Class represents the post functions on the admin panel
    """
    list_display = ('name', 'price', 'rating', )
    search_fields = ['name']

    ordering = ('price',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
