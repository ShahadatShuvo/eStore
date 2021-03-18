from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'price', 'category', 'digital', 'inStock', 'soldout',
    ]

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'date_ordered', 'complete', 'transaction_id',
    ]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
       'quantity', 'date_added',
    ]

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = [
       'address', 'city', 'state', 'date_added',
    ]


admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)