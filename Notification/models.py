from django.db import models
from django.utils import timezone

NOTIFICATION_TYPE = 'SYSTEM'

priority_choices = [
    ('Low', '🟢 Low'),
    ('Medium', '🟠 Medium'),
    ('High', '🔴 High'),
    ('Critical', '🔴🔴🔴 Critical'),
]


class Notification(models.Model):
    noti_id = models.AutoField(primary_key=True)
    log = models.ForeignKey('log.Log', on_delete=models.CASCADE, null=True, blank=True)
    sender_id = models.IntegerField(null=True, blank=True)
    receiver_id = models.IntegerField(null=True, blank=True)
    visitor_type = models.CharField(max_length=50, blank=True, null=True)
    topic = models.CharField(max_length=150)
    notification_type = models.CharField(max_length=20, default=NOTIFICATION_TYPE, editable=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)
    is_seen = models.BooleanField(default=False)
    priority = models.CharField(max_length=30, choices=priority_choices, default='Medium')

    class Meta:
        db_table = 'notification_center'
        ordering = ['-created_at']

    def mark_read(self):
        if not self.is_seen:
            self.is_seen = True
            self.read_at = timezone.now()
            self.save(update_fields=['is_seen', 'read_at'])

    def __str__(self):
        return f'[{self.priority}]: {self.topic} -> receiver:{self.receiver_id}'
