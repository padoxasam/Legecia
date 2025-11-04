from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    biometric_inf = models.CharField(max_length= 512 ,null=True)
    qr_token= models.CharField(max_length=512 , blank=True , null=True)
    device_verified =models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)






    def __str__(self):
        return self.username
    