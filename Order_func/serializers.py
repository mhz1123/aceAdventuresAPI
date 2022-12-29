from rest_framework import serializers
from .models import Address, Order


class getAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address_id','house_num', 'street', 'area','city' ,'zip_code', 'district', 'state','country']

class createAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['house_num', 'street', 'area','city' ,'zip_code', 'district', 'state','country']

class createOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product_id','sp_id','quantity','total_amt','order_date','shipping_address','status']

class updateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']