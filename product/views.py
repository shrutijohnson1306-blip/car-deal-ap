from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer

def product_list(request):
    products = Product.objects.all()
    if not products:
        return HttpResponse("No products found in the database")
    return render(request, 'product/product_list.html', {'products': products})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer