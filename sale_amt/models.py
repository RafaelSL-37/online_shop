from django.db import models
from products.models import Product

class SaleAmount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.product.name
