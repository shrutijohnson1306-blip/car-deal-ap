from django.db import models

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    vehicle_maker = models.CharField(max_length=60, null=True, blank=True)
    vehicle_model = models.CharField(max_length=60, null=True, blank=True)
    vehicle_color = models.CharField(max_length=60, null=True, blank=True)
    vehicle_model_year = models.IntegerField(null=True, blank=True)
    vehicle_price = models.DecimalField(max_digits=14, decimal_places=8, null=True, blank=True)

    class Meta:
        db_table = "product_t"

