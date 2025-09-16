"""
URL configuration for main_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# main_project/urls.py
from django.contrib import admin
from django.urls import path, include
from customer import views as customer_views
from product import views as product_views 
from order import views as order_views  
from shipper import views as shipper_views
from . import views as main_views
from rest_framework.routers import DefaultRouter
from accounts import views as accounts_views

# Import API viewsets
from customer.views import CustomerViewSet
from product.views import ProductViewSet
from order.views import OrderViewSet
from shipper.views import ShipperViewSet

# Create router for DRF
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'shippers', ShipperViewSet)

urlpatterns = [
    # Homepage
    path('', main_views.home, name='home'),

    # Django admin
    path('admin/', admin.site.urls),

    # HTML views
    path('customers/', customer_views.customer_list, name='customer_list'),
    path('products/', product_views.product_list, name='product_list'),  
    path('orders/', order_views.order_list, name='order_list'),
    path('shippers/', shipper_views.shipper_list, name='shipper_list'),

    # API routes
    path('api/', include(router.urls)),
    
    # User Authentication
    path("accounts/register/", accounts_views.register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")), 
    
    path("analytics/", include("analytics.urls")),

]


