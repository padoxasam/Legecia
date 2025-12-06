from django.db import models

# Create your models here.
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone

notification_types=[ ('EMAIL','EMAIL'),
                    ('Push','Push'),
                    ('In App','In App'),
                    ('SMS','SMS'),
                    ('System','System'),
                    ('Unlock','Unlock'),

]
priority_choices=  [('Low', '🟢 Low'),
                     ('Medium','"🟠 Medium'),
                     ('High','🔴 High'),
                     ('Critical','🔴🔴🔴 Critical'),
                     ]
class Notification(models.Model):
    noti_id=models.AutoField(primary_key=True)
    sender_content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE,related_name='Notification_Senders',null=True,blank=True)
    sender_object_id=models.PositiveBigIntegerField(null=True,blank=True)
    sender=GenericForeignKey('sender_content_type','sender_object_id')
    receiver_content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE,related_name='Notification_Receivers',null=True,blank=True)
    receiver_object_id=models.PositiveBigIntegerField(null=True,blank=True)
    receiver=GenericForeignKey('receiver_content_type','receiver_object_id')
    log=models.ForeignKey('log.Log',on_delete=models.CASCADE,null=True,blank=True)
    visitor_type=models.CharField(max_length=50,blank=True,null=True)
    topic=models.CharField(max_length=150)
    notification_type=models.CharField(max_length=30,choices=notification_types)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    read_at=models.DateTimeField(null=True,blank=True)
    is_seen=models.BooleanField(default=False)
    priority=models.CharField(max_length=30,choices=priority_choices,default='Medium')
    class Meta:
        db_table='notification_center'
        ordering=['-created_at']
        
    def mark_read(self):
        if not self.is_seen:
            self.is_seen=True
            self.read_at=timezone.now()
            self.save(update_fields=['is_seen','read_at'])
    def __str__(self):
        return f'[{self.priority}]:{self.topic} -> {self.receiver}'