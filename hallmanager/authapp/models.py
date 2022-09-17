from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Nuser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    blocked = models.BooleanField()
    phone = models.CharField(max_length=15)
    isAdmin = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user.username)