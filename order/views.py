from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
from rest_framework import viewsets
from .serializers import OrderSerializer
from django.db.models import Count
from customer.models import Customer


def order_list(request):
    orders = Order.objects.all()
    if not orders:
        return HttpResponse("No orders found in the database")
    return render(request, 'order/order_list.html', {'orders': orders})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
def customers_by_state(request):
    # count unique customers per state
    data = Customer.objects.filter(order__isnull=False).values("state").annotate(
        total_customers=Count("customer_id", distinct=True)
    ).order_by("state")

    return render(request, "order/customers_by_state.html", {"data": data})
