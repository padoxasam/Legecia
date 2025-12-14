from django.contrib.contenttypes.models import ContentType
from user_registration.models import User
from .models import Notification
def create_notification(
    sender_id,
    receiver_id,
    visitor_type,
    topic,
    message,
    notification_type='System',
    priority='Medium',
    log_id=None
):
    user_ct = ContentType.objects.get_for_model(User)

    return Notification.objects.create(
        sender_content_type=user_ct,
        sender_object_id=sender_id,
        receiver_content_type=user_ct,
        receiver_object_id=receiver_id,
        visitor_type=visitor_type,  # OK to keep
        topic=topic,
        message=message,
        notification_type=notification_type,
        priority=priority,
        log_id=log_id
    )
