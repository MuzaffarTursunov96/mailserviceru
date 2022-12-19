from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated



class ListCustomers(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer 

class DetailCustomers(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer 
    lookup_url_kwarg='pk'


class CreateCustomers(generics.CreateAPIView):
    queryset = Customer.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer 

class UpdateCustomers(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer 
    lookup_url_kwarg='pk'

class DeleteCustomers(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer 
    lookup_url_kwarg='pk'