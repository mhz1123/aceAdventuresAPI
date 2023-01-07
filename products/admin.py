from django.contrib import admin
from .models import Product, SpareParts
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name','product_price', 'product_img_url','product_image', 'product_spec', 'inStock']

@admin.register(SpareParts)
class SparePartsAdmin(admin.ModelAdmin):
    list_display = ['sp_id', 'sp_name', 'sp_price', 'sp_img_url', 'inStock']