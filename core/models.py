from django.db import models
from django.conf import settings
User=settings.AUTH_USER_MODEL
class CoreProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='core profile')
    phone_num=models.CharField(max_length=15)
    gender=models.CharField(max_length=10)
    dob=models.DateField(null=True,blank=True)
    family_title=models.CharField(max_length=100,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    region = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.user.username