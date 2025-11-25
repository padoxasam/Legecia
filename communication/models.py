from django.db import models

# Create your models here.
from user_registration.models import User,Beneficiary,Guardian

class communicationMeans(models.Model):
    u=models.ForeignKey(User,on_delete=models.CASCADE)
    b_u=models.ForeignKey(Beneficiary,on_delete=models.CASCADE)
    us_email=models.EmailField(max_length=100,unique=True)
    us_email=models.EmailField(max_length=100,unique=True)
    #packg=models.ForeignKey(Package,on_delete=models.CASCADE)
    relation_choices= ( 
                        ('MOTHER','MOTHER'),
                       ('FATHER','FATHER'),
                       ('GRANDMOTHER','GRANDMOTHER'),
                       ('GRANDFATHER','GRANDFATHER'),
                       ('STEP FATHER','STEP FATHER'),
                       ('STEP MOTHER','STEP MOTHER'),
                       ('BROTHER','BROTHER'),
                       ('SISTER','SISTER'),
                       ('UNCLE','UNCLE'),
                       ('AUNT','AUNT'),
                       ('COUNIN','COUSIN'),
                       ('NEPHEW','NEPHEW'),
                       ('NIECE','NIECE'),
                       ('FAMILY FRIEND','FAMILY FRIEND'),
                       ('NEIGHBOR','NEIGHBOR'),
                       ('MENTOR','MENTOR'),
                       ('SOCIAL WORKER','SOCIAL WORKER'),
                       ('OTHER','OTHER'),
                       
                        ('LEGEAL GUARDIAN','LEGEAL GUARDIAN'),
                        ('FOSTER PARENT','FOSTER PARENT'),
                        ('CARETAKER','CARETAKER'),

    )
    relationship=models.CharField(max_length=50,choices=relation_choices)

    com_m1= models.CharField(max_length=300)
    com_m2=models.CharField(max_length=300,blank= True, null= True)
    additional_comments=models.TextField(blank=True,null=True)
    class meta:
        db_table='communication_means'

    def __str__ (self):
        return f'Communcation via Email User :{self.us_email}\nCommuncation via Beneficiary:{self.be_email} '
    