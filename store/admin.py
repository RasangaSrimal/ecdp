from django.contrib import admin
from .models import Customer, Order, OrderItem, ShippingAddress, Category, Product

# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'digital', 'in_stock', 'is_active']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
