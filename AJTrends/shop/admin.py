from django.contrib import admin
from .models import Product, Category, Order


# Register models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)  # Add a filter for categories
    search_fields = ('name', 'category__name')  # Enable search by category


# Register the models with the admin site
admin.site.register(Product, ProductAdmin)  # Register Product with ProductAdmin
admin.site.register(Category)
admin.site.register(Order)
