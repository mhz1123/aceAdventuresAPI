from rest_framework import serializers
from .models import Product, SpareParts

class ProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product_name = serializers.CharField(max_length=100)
    product_price = serializers.DecimalField(max_digits = 10, decimal_places=2)
    product_img_url = serializers.URLField(max_length=100)
    product_description = serializers.CharField(max_length=1000)
    product_feature = serializers.CharField(max_length=1000)
    product_spec = serializers.CharField(max_length=1000)
    inStock = serializers.BooleanField(default=True)

class SparePartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpareParts
        fields = '__all__'