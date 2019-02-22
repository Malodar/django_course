from django.contrib import admin
from .models import Category, Product, CartItem, Cart


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {'slug': ('category_name', )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'price', 'description', 'image', 'owner']
    list_filter = ['name']
    list_editable = ['price', 'category', 'description', 'owner']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartItem)
admin.site.register(Cart)
