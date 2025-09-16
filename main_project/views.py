from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum, Avg
from order.models import Order
from customer.models import Customer
from product.models import Product
from shipper.models import Shipper

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, "home.html")

@login_required(login_url='/accounts/login/')
def customers_by_state(request):  # Q1
    data = Customer.objects.values('state').annotate(total_customers=Count('customer_id', distinct=True))
    return render(request, "analytics/customers_by_state.html", {"data": data})

@login_required(login_url='/accounts/login/')
def orders_by_quarter(request):  # Q2
    data = Order.objects.values('quarter_number').annotate(total_orders=Count('order_id'))
    return render(request, "analytics/orders_by_quarter.html", {"data": data})

@login_required(login_url='/accounts/login/')
def revenue_by_state(request):  # Q3
    data = Order.objects.values('customer__state').annotate(total_revenue=Sum('quantity'))
    return render(request, "analytics/revenue_by_state.html", {"data": data})

@login_required(login_url='/accounts/login/')
def top_products(request):  # Q4
    data = Order.objects.values('product').annotate(total_sold=Sum('quantity')).order_by('-total_sold')[:10]
    return render(request, "analytics/top_products.html", {"data": data})

@login_required(login_url='/accounts/login/')
def revenue_trend(request):  # Q5
    data = Order.objects.values('quarter_number').annotate(revenue=Sum('quantity'))
    return render(request, "analytics/revenue_trend.html", {"data": data})

@login_required(login_url='/accounts/login/')
def avg_discount_by_shipmode(request):  # Q6
    data = Order.objects.values('ship_mode').annotate(avg_discount=Avg('discount'))
    return render(request, "analytics/avg_discount_by_shipmode.html", {"data": data})

@login_required(login_url='/accounts/login/')
def customer_lifetime_value(request):  # Q7
    data = Order.objects.values('customer__customer_name').annotate(total_value=Sum('quantity'))
    return render(request, "analytics/customer_lifetime_value.html", {"data": data})

@login_required(login_url='/accounts/login/')
def orders_by_shipper(request):  # Q8
    data = Order.objects.values('shipper__shipper_name').annotate(total_orders=Count('order_id'))
    return render(request, "analytics/orders_by_shipper.html", {"data": data})

@login_required(login_url='/accounts/login/')
def high_value_customers(request):  # Q9
    data = Order.objects.values('customer__customer_name').annotate(total_spent=Sum('quantity')).order_by('-total_spent')[:5]
    return render(request, "analytics/high_value_customers.html", {"data": data})

@login_required(login_url='/accounts/login/')
def revenue_by_product_category(request):  # Q10
    data = Product.objects.values('vehicle_maker').annotate(total_revenue=Sum('vehicle_price'))
    return render(request, "analytics/revenue_by_product_category.html", {"data": data})
