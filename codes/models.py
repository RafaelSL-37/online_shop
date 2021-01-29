from django.db import models

class Code(models.Model):
    code = models.CharField(max_length=100)
    promo_start = models.DateTimeField(auto_now_add=True)
    promo_end = models.DateTimeField()

    def __str__(self):
        return self.code