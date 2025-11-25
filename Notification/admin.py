from django.contrib import admin

# Register your models here.
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "noti_id",
        "topic",
        "notification_type",
        "priority",
        "sender_id",
        "receiver_id",
        "created_at",
        "is_seen",
    )
    list_filter = ("priority", "notification_type", "is_seen")
    search_fields = ("topic", "message", "receiver_id")