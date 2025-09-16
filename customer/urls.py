from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, customer_list

# Router for API
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    # HTML view
    path('', customer_list, name='customer_list'),

    # API endpoints
    path('api/', include(router.urls)),
]
