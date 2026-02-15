from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('noti_id', 'topic', 'message', 'sender_id', 'receiver_id', 'priority', 'is_seen', 'created_at')
    list_filter = ('priority', 'is_seen')
    search_fields = ('topic', 'message')
