from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

class CategoryViewSet(viewsets.ViewSet):
        '''
            A simple viewset for viewing categories.
        '''

        queryset = Category.objects.all()

# Decorator:- A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. They are an excellent way to apply reusable functionality across multiple functions, such as timing, caching, logging, or authentication.

        @extend_schema(responses = CategorySerializer)
        def list(self, request):
                serializer = CategorySerializer(self.queryset, many=True)
                return Response(serializer.data)
        
class BrandViewSet(viewsets.ViewSet):
        '''
            A simple viewset for viewing brands.
        '''

        queryset = Brand.objects.all()

        @extend_schema(responses = BrandSerializer)
        def list(self, request):
                serializer = BrandSerializer(self.queryset, many=True)
                return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
        '''
            A simple viewset for viewing products.
        '''

        queryset = Product.objects.all()

        @extend_schema(responses = ProductSerializer)
        def list(self, request):
                serializer = ProductSerializer(self.queryset, many=True)
                return Response(serializer.data)