from django.db import models

# Create your models here.
from package.models import Package
from user_registration.models import User,Beneficiary,Guardian

packyia_Types=[    ('LOCKED','Locked Supervision'),
                    ('Timed', 'Timed Unlock'),
                    ('Manual','Guardian Manual Unlock'), ]
Guardian_status=[('Pending','Waiting for Guardian Sign up'),
                    ('Active','Active Guardian'),]
User_status= [('Active','Active'),('Departed','Passed Away'),]
class SupervisedPack(models.Model):
    pack=models.OneToOneField(Package,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bene=models.ForeignKey(Beneficiary,on_delete=models.CASCADE)
    guard=models.ForeignKey(Guardian,on_delete=models.CASCADE)
    packat=models.CharField(max_length=50 ,choices=packyia_Types)
    guadian_control=models.BooleanField(default=True)
    guardian_revealing=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    guard_stat=models.CharField(max_length=20,choices=Guardian_status)
    user_stat=models.CharField(max_length=20,choices=User_status)
    remarks=models.TextField(null=True,blank=True)
    class Meta:
        db_table='supervised_packs'
    def __str__(self):
        return f'supervision for Package: {self.pck.pack_name}'