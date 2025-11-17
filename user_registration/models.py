from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    biometric_inf = models.CharField(max_length= 512 ,null=True)
    qr_token= models.CharField(max_length=512 , blank=True , null=True)
    device_verified =models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)

    full_name=models.CharField(max_length=200, null=False,blank=True)
    def save(self,*args,**kwargs):
        if not self.full_name:
            self.full_name = f'{self.first_name}{self.last_name}'.strip()
        super().save(*args,**kwargs)



    def __str__(self):
        return self.username

class Beneficiary(models.Model):
    b_full_name = models.CharField(max_length=255)
    b_email = models.EmailField()
    b_username = models.CharField(max_length=255)

    def __str__(self):
        return self.b_username    
class Guardian(models.Model):
    g_full_name = models.CharField(max_length=255)
    g_email = models.EmailField()
    g_username = models.CharField(max_length=255)

    def __str__(self):
        return self.g_username
