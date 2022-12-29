from .models import Product, SpareParts
from .serializers import ProductDetailSerializer, SparePartsSerializer, ProductSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def product_list(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many = True)
    return JsonResponse(serializer.data, safe= False)

@api_view(['GET'])
def product_details(request, pk):
    product = Product.objects.all().filter(product_id=pk)
    serializer = ProductDetailSerializer(product, many= True)
    return JsonResponse(serializer.data, safe= False)

@api_view(['GET'])
def spareParts(request, pk):
    product = SpareParts.objects.all().filter(product_id = pk)
    serializer = SparePartsSerializer(product, many = True)
    return JsonResponse(serializer.data, safe= False)
