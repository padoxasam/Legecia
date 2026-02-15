from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'noti_id', 'sender_id', 'receiver_id', 'log',
            'visitor_type', 'topic', 'notification_type',
            'message', 'created_at', 'read_at', 'is_seen', 'priority',
        ]
        read_only_fields = ['created_at', 'read_at']
