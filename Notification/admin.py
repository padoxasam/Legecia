from django.contrib import admin

# Register your models here.
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "noti_id",
        "topic",
        "priority",
        'sender',
        'receiver',
        "created_at",
        "is_seen",
        
    )
    
    list_filter = ("priority", "notification_type", "is_seen")
    search_fields = ("topic", "message")