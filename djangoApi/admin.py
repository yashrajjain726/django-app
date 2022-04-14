from django.contrib import admin

# Register your models here.
from djangoApi.models import Product, Operation


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'measurement_unit']


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ['date', 'id', 'direction', 'amount']

