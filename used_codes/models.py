from django.db import models
from django.contrib.auth.models import User
from codes.models import Code

class UsedCode(models.Model):
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    use = models.BooleanField(default=False)

    def __str__(self):
        return self.code.code