from django.shortcuts import render
from .models import Customer
from rest_framework import viewsets
from .serializers import CustomerSerializer
from django.contrib.auth.decorators import login_required


# Existing HTML view
@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customer/customer_list.html", {"customers": customers})

# New API ViewSet
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'customer_id' 





