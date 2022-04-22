
from dataclasses import field
from functools import partial
from unittest.util import _MAX_LENGTH
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Items
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,permission_classes
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny


# Create your views here.
class ItemsSerializer(serializers.ModelSerializer):
    item_name=serializers.CharField(max_length=200)
    item_price=serializers.CharField(max_length=100)
    item_qty=serializers.CharField(max_length=200)
    class Meta:
        model=Items
        fields=['item_name','item_price','item_qty']

# class Itemsview(APIView):
#     def post(self,request):
#         serializer=ItemsSerializer(data=request.data)
#         print("post")
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
#         return Response({"status":"error","data":serializer.error},status=status.HTTP_400_BAD_REQUEST)

#     def get(self,pk):
#         items=Items.objects.get(id=pk)
#         print("get")
#         serializer=ItemsSerializer(items,many=True)
#         return Response({"status":"sucess","data":serializer.data},status=status.HTTP_200_OK)

@api_view(["GET"])
def displayAll(request):
    items=Items.objects.all()
    print("getAll")
    serializer=ItemsSerializer(items,many=True)
    return Response({"status":"sucess","data":serializer.data},status=status.HTTP_200_OK)

@api_view(["GET"])
def displayOne(request,pk):
    item=Items.objects.get(id=pk)
    print("getOne")
    serializer = ItemsSerializer(item)
    return Response({"status":"sucess","data":serializer.data},status=status.HTTP_200_OK)

@api_view(["POST"])
def add(request):
    serializer=ItemsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status":"sucess","data":serializer.data},status=status.HTTP_200_OK)
    else:
        return Response({"status":"error","data":serializer.error},status=status.HTTP_400_BAD_REQUEST)

@api_view(["PATCH"])
def update(request,id):
    item=Items.objects.get(id=id)
    serializer=ItemsSerializer(item,request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status":"sucess","data":serializer.data})
    else:
        return Response({"status":"error","data":serializer.error})

@api_view(["DELETE"])
def remove(request,id):
    item=get_object_or_404(Items,id=id)
    item.delete()
    return Response({"status":"sucess","data":"deleted item"})

@api_view(["POST"])
@csrf_exempt
def login_page(request):
    username=request.data.get('username')
    password=request.data.get('password')
    if username is None or password is None:
        return Response({"status":"Error",})
    user=authenticate(username=username,password=password)
    if not user:
        return Response({"status":"invalid credentialds"})
    token,_=Token.objects.get_or_create(user=user)
    return Response({"token":token.key},status=status.HTTP_200_OK)


    

