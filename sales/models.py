from django.db import models
from django.contrib.auth.models import User
from sale_amt.models import SaleAmount

class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    sale_amount = models.ManyToManyField(SaleAmount)
    date = models.DateTimeField(auto_now_add=True)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username