from django.urls import path
from . import views

urlpatterns = [
    path("customers_by_state/", views.customers_by_state, name="customers_by_state"),
    path("top_vehicle_makers/", views.top_vehicle_makers, name="top_vehicle_makers"),
    path("preferred_maker_by_state/", views.preferred_maker_by_state, name="preferred_maker_by_state"),
    path("avg_rating_by_quarter/", views.avg_rating_by_quarter, name="avg_rating_by_quarter"),
    path("feedback_distribution/", views.feedback_distribution, name="feedback_distribution"),
    path("orders_by_quarter/", views.orders_by_quarter, name="orders_by_quarter"),
    path("revenue_change/", views.revenue_change, name="revenue_change"),
    path("revenue_orders_trend/", views.revenue_orders_trend, name="revenue_orders_trend"),
    path("avg_discount_by_card/", views.avg_discount_by_card, name="avg_discount_by_card"),
    path("shipping_time/", views.shipping_time, name="shipping_time"),
]
