from django.db import models

# Create your models here.
from log.models import Log
class AccessLog(models.Model):
    access_id=models.AutoField(primary_key=True)
    log=models.ForeignKey(Log,on_delete=models.CASCADE)
    ip_address=models.GenericIPAddressField()
    device_info=models.CharField(max_length=200,null=True,blank=True)
    login_start=models.DateTimeField(auto_now_add=True)
    logout=models.DateTimeField(null=True,blank=True)
    successful_log=models.BooleanField(default=True)
    failure_message=models.TextField(null=True,blank=True)
    class Meta:
        db_table='access_logs'
        ordering=['-login_start']
    def __str__(self):
        return f'AccessLog #{self.access_id}\nAddress:{self.ip_address}'
    