from django.contrib import admin
from .models import Address, Order
# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','address_id','house_num','street','area','city','zip_code','district','state','country']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','order_id','product','sp','quantity','total_amt','order_date','address','status']