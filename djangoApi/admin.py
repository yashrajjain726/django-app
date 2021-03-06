from django.contrib import admin

from djangoApi.models import Product, Operation


# Adding Model Fields as an Admin to show it in AdminPanel
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'name', 'measurement_unit']


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'date', 'direction', 'amount']
