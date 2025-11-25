from django.db import models

# Create your models here.
from django.conf import settings

pack_status_choices=[('Active','Active'),
                     ('Archived','Archived'),
                     ]
Delivery_choices= [('Direct','Direct'),
                   ('Guardian','Guardian'),
                   ('Public','Public'),
                   ]
pacK_type_choices=[('Event-Based','Event-Based'),
                   ('Location-Based','Location-Based'),
                   ('Countdown','Countdown'),]

class Package(models.Model):
    pack_id=models.BigAutoField(primary_key=True)
    owner=models.IntegerField()
    ownership=models.CharField(max_length=200,null=False)
    uploaded_on=models.DateField(null=False)
    pack_name=models.CharField(max_length=50,null=False)
    last_modification=models.DateField(null=False)
    pack_status=models.CharField(max_length=20,choices=pack_status_choices)
    tags=models.CharField(max_length=300,null=True)
    pack_delivery=models.CharField(max_length=20,choices=Delivery_choices)
    pack_type=models.CharField(max_length=30,choices=pacK_type_choices)
    total_files=models.IntegerField(default=0)
    has_expiry=models.BooleanField(default=False)
    expiry_at= models.DateField(null=True)
    unlocked=models.BooleanField(default=False)
    description=models.TextField(null=True,blank=True)

    class Meta:
        db_table='package'
        managed=False
        ordering= ['-uploaded_on']
    def __str__(self):
        return f'{self.pack_name or self.pack_id} (owner={self.owner})'
    