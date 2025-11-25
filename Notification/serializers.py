from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType

class NotificationSerializer(serializers.ModelSerializer):
    sender_type=serializers.SerializerMethodField(read_only=True)
    receiver_type=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=Notification
        fields=["id",
            "sender_content_type",
            "sender_object_id",
            "sender_type",
            "receiver_content_type",
            "receiver_object_id",
            "receiver_type",
            "log",
            "visitor_type",
            "topic",
            "notification_type",
            "message",
            "created_at",
            "read_at",
            "is_seen",
            "priority",
            ]
        read_only_fields=['created_at','read_at']
    def get_sender_type(self,obj):
        if obj.sender_content_type:
            return obj.sender_content_type.model_class().__name__
        return None
    def get_receiver_type(self,obj):
        if obj.receiver.content_type:
            return obj.receiver_content_type.model_class().__name__
        return None
    def validate(self, data):
        receiver_cont_type=data.get('receiver_content_type') or self.instance or self.instance.receiver_content_type
        receiver_ob_id=data.get('receiver_object_id') or self.instance and self.instance.receiver_object_id
        if not receiver_cont_type and receiver_ob_id:
            raise serializers.ValidationError('Receiver Content Type and object id must be provided ')