from django.db import models
from ratings.models import Rating

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    sold = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    ratings = models.ManyToManyField(Rating, blank=True)
    image = models.ImageField(upload_to='shop', null=True, blank=True)

    def __str__(self):
        return self.name