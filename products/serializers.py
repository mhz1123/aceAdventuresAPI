from rest_framework import serializers
from .models import Product, SpareParts

class ProductDetailSerializer(serializers.ModelSerializer):
    # product_id = serializers.IntegerField()
    # product_name = serializers.CharField(max_length=100)
    # product_price = serializers.DecimalField(max_digits = 10, decimal_places=2)
    # product_img_url = serializers.URLField(max_length=100)
    # product_description = serializers.CharField(max_length=1000)
    # product_feature = serializers.CharField(max_length=1000)
    # product_spec = serializers.CharField(max_length=1000)
    # inStock = serializers.BooleanField(default=True)
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'product_price', 'product_img_url', 'inStock']

class SparePartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpareParts
        fields = '__all__'
