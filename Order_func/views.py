from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Address, Order
from Customer.models import User
from .serializers import getAddressSerializer, createAddressSerializer, createOrderSerializer, updateOrderSerializer
from rest_framework.permissions import IsAuthenticated
from Customer.renderers import UserRenderer

@api_view(['GET'])
def get_address(request, pk):
    renderer_classes = [UserRenderer]
    # permission_classes = [IsAuthenticated]
    address = Address.objects.all().filter(user=pk)
    serializer = getAddressSerializer(address, many = True)
    return JsonResponse(serializer.data, safe= False)

@api_view(['POST'])
def create_address(request, pk):
    renderer_classes = [UserRenderer]
    data = request.data
    address = Address.objects.create(
        user_id = pk,
        house_num = data['house_num'],
        street = data['street'],
        area = data['area'],
        city = data['city'],
        zip_code = data['zip_code'],
        district = data['district'],
        state = data['state'],
        country = data['country']
    ).save()
    serializer = createAddressSerializer(address, many = True)
    return Response({'msg':'Address created Successfully'}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_address(request, pk):
    renderer_classes = [UserRenderer]
    address = Address.objects.get(address_id = pk)
    serializer = createAddressSerializer(address, data= request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'msg':'Address updated Successfully'}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_address(request, pk):
    renderer_classes = [UserRenderer]
    address = Address.objects.get(address_id = pk)
    address.delete()
    return Response({'msg':'Address deleted Successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_order(request, uk,ak,pk = None,sk = None):
    renderer_classes = [UserRenderer]
    data = request.data
    order = Order.objects.create(
        user_id = uk,
        product_id = pk,
        sp_id = sk,
        quantity = data['quantity'],
        total_amt = data['total_amt'],
        order_date = data['order_date'],
        address = Address.objects.get(address_id=ak),
        status = data['status']
    ).save()
    serializer = createOrderSerializer(order, many=True)
    return Response({'msg':'Order created Successfully'}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_order(request, ok):
    renderer_classes = [UserRenderer]
    order = Order.objects.get(order_id = ok)
    serializer = updateOrderSerializer(order, data= request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'msg':'Order updated Successfully'}, status=status.HTTP_200_OK)