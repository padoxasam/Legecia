from .models import Notification


def create_notification(
    sender_id,
    receiver_id,
    visitor_type,
    topic,
    message,
    notification_type='SYSTEM',
    priority='Medium',
    log_id=None,
):
    return Notification.objects.create(
        sender_id=sender_id,
        receiver_id=receiver_id,
        visitor_type=visitor_type,
        topic=topic,
        message=message,
        priority=priority,
        log_id=log_id,
    )
