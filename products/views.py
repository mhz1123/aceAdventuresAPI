from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product, SpareParts
from .serializers import ProductSerializer, SparePartsSerializer
from django.http import JsonResponse
# Create your views here.

def product_details(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many = True)
    return JsonResponse(serializer.data, safe= False)

def spareParts(request, pk):
    product = SpareParts.objects.all().filter(product_id = pk)
    serializer = SparePartsSerializer(product, many = True)
    return JsonResponse(serializer.data, safe= False)