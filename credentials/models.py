from django.db import models

# Create your models here.
from log.models import Log
import uuid
class Credenntials(models.Model):
    credential_id=models.AutoField(primary_key=True)
    log=models.ForeignKey(Log,on_delete=models.CASCADE,null=True,blank=True)
    username=models.CharField(max_length=200,unique=True)
    password_hashed=models.TextField()
    password_salt=models.TextField()
    security_qu1=models.CharField(max_length=200)
    security_qu2=models.CharField(max_length=200)
    security_ans1=models.CharField(max_length=200)
    security_ans2=models.CharField(max_length=200)
    recover_email=models.CharField(max_length=100,unique=True)
    two_factor=models.BooleanField(default=False)
    two_factor_token=models.TextField(null=True,blank=True)
    password_change=models.DateTimeField(auto_now_add=True)
    last_seen=models.DateTimeField(null=True,blank=True)
    failed_entry=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
class Meta:
    db_table='credentials'
def __str__(self):
    return f'Credentials For {self.username}'
