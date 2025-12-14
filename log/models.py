from django.db import models

# Create your models here.
visitor_type_choices= [('Guardian','Guardian'),
                       ('User','User'),
                       ('Beneficiary','Beneficiary'),

]
log_acions=[("LOGIN_SUCCESS", "User login success"),
    ("LOGIN_FAILED", "User login failed"),
    ("LOGOUT", "User logged out"),
    ("ACCOUNT_CREATED", "New account created"),
    ("ACCOUNT_VERIFIED", "User verified email"),
    ("ACCOUNT_UPDATED", "User updated profile"),
    ("PASSWORD_CHANGED", "Password updated"),
    ("PACKAGE_CREATED", "New package created"),
    ("PACKAGE_UPDATED", "Package modified"),
    ("PACKAGE_DELETED", "Package deleted"),
    ("PACKAGE_UNLOCKED", "Package unlocked"),("GUARDIAN_ASSIGNED", "Guardian assigned"),
    ("GUARDIAN_REMOVED", "Guardian removed"),("BENEFICIARY_CONNECTED", "Beneficiary connected"),
    ("BENEFICIARY_UPDATED", "Beneficiary profile updated"),("COMMUNICATION_SENT", "Communication sent"),
    ("COMMUNICATION_UPDATED", "Communication updated"), ("SYSTEM_EVENT", "System generated log")

]
class Log(models.Model):
    log_id=models.AutoField(primary_key=True)

    visitor_id=models.IntegerField()
    ip_address=models.GenericIPAddressField()
    log_action=models.CharField(max_length=100,choices=log_acions)
    log_at=models.DateTimeField(auto_now_add=True)
    additional_comments=models.TextField(blank=True,null=True)
    device_info=models.TextField(blank=True,null=True)
    region=models.CharField(max_length=100,null=True,blank=True)
    log_stat=models.CharField(max_length=30,default='Successful !')
    class Meta:
        db_table='logs'
    def __str__(self):
        return f'{self.log_action} by {self.visitor_type}\n ID:{self.visitor_id}'  
          