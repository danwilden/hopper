# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Business, User, Financial, DataType, Listing, Viewer, Contact
from .serializers import *
from rest_framework import status , generics , mixins

from .data.projection import execute
from .forms import SignUpForm
# Create your views here.

class business_list(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class business_detail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Business.objects.all()
     serializer_class =  BusinessSerializer

class user_list(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class user_detail(generics.RetrieveUpdateDestroyAPIView):
     queryset = User.objects.all()
     serializer_class =  UserSerializer

class viewer_list(generics.ListCreateAPIView):
    queryset = Viewer.objects.all()
    serializer_class = ViewerSerializer

class viewer_detail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Viewer.objects.all()
     serializer_class =  ViewerSerializer

class contact_list(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class contact_detail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Contact.objects.all()
     serializer_class =  ContactSerializer

class listing_list(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class listing_detail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Listing.objects.all()
     serializer_class =  ListingSerializer

class financial_list(generics.ListCreateAPIView):
    queryset = Financial.objects.all()
    serializer_class = FinancialSerializer

class financial_detail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Financial.objects.all()
     serializer_class =  FinancialSerializer

class datatype_list(generics.ListCreateAPIView):
    queryset = DataType.objects.all()
    serializer_class = DataTypeSerializer

class datatype_detail(generics.RetrieveUpdateDestroyAPIView):
     queryset = DataType.objects.all()
     serializer_class =  DataTypeSerializer

class valuation_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Valuation.objects.all()
    serializer_class = ValuationSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.POST._mutable:
            request.POST._mutable = True
        request.data
        request.data['high'], request.data['middle'], request.data['low'] = execute(float(request.data['sigma']), float(request.data['mu']), float(request.data['start']), float(request.data['equity']),float(request.data['debt']),float(request.data['eroi']), float(request.data['cod']))
        return self.create(request, *args, **kwargs)



def test(request):
     check = 5
     return render(request, 'demoapp/home.html', {test: check})

#
# @api_view(['GET', 'POST'])
# def product_list(request):
#     """
#     List all products, or create a new product.
#     """
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products,context={'request': request} ,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, pk):
#     """
#     Retrieve, update or delete a product instance.
#     """
#     try:
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ProductSerializer(product,context={'request': request})
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# class family_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Family.objects.all()
#     serializer_class = FamilySerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         print("Maybe I can do functions here")
#         return self.create(request, *args, **kwargs)
#
# class family_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Family.objects.all()
#     serializer_class = FamilySerializer
#
# class location_list(generics.ListCreateAPIView):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer
#
# class location_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Location.objects.all()
#     serializer_class =  LocationSerializer
#
# class transaction_list(generics.ListCreateAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
#
# class transaction_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class =  TransactionSerializer
