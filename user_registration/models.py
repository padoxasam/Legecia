from django.db import models
import AbstractUser from django.contrib.auth.models

class user (AbstractUser):

    biometric_inf = models.CharField(max_length= 512 ,null=True)
    qr_token= models.CharField(max_length=512 , blank=True , null=True)
    device_verified =models.BooleanField(default=False)
    

    def __str__(self):
        return self.username