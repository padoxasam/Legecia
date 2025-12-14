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
STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Pending', 'Pending Approval'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
class SupervisedPack(models.Model):
    pack = models.OneToOneField(
        Package,
        on_delete=models.CASCADE,
        related_name='supervision') 
    pack_name = models.CharField(max_length=50, null=True, blank=True)  # New field
   
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bene=models.ForeignKey(Beneficiary,on_delete=models.CASCADE)
    guard=models.ForeignKey(Guardian,on_delete=models.CASCADE)
    packat=models.CharField(max_length=50 ,choices=packyia_Types)
    supervision_end = models.DateTimeField(null=True, blank=True)
    supervision_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')

    guardian_revealing=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    guard_stat=models.CharField(max_length=20,choices=Guardian_status)
    user_stat=models.CharField(max_length=20,choices=User_status)
    remarks=models.TextField(null=True,blank=True)
    class Meta:
        db_table='supervised_packs'
    def save(self,*args,**kwargs):
        if self.pack:
            self.pack_name= self.pack.pack_name
        super().save(*args,**kwargs)
        
    def __str__(self):
        return f'supervision for Package: {self.pack.pack_name}'