from django.contrib import admin

# Register your models here.
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('noti_id',
    'message',
    'sender',
    'receiver',
    'created_at',)

    def sender(self, obj):
        return obj.from_user

    def receiver(self, obj):
        return obj.to_user
