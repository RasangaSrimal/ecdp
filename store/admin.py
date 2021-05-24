from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'catogory', 'price', 'digital', 'in_stock']
    list_filter = ['in_stock']
    list_editable = ['price', 'in_stock']
