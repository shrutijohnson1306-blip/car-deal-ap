from django.db import models
from customer.models import Customer
from product.models import Product
from shipper.models import Shipper

class Order(models.Model):
    order_id = models.CharField(max_length=25, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column="customer_id", null=True, blank=True)
    shipper = models.ForeignKey(Shipper, on_delete=models.SET_NULL, db_column="shipper_id", null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, db_column="product_id", null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    vehicle_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    ship_date = models.DateField(null=True, blank=True)
    discount = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    ship_mode = models.CharField(max_length=25, null=True, blank=True)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    customer_feedback = models.CharField(max_length=20, null=True, blank=True)
    quarter_number = models.IntegerField(null=True, blank=True)
    delivery_type = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = "order_t"


