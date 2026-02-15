from .models import Log


def create_log(visitor_id, log_action, ip_address, **kwargs):
    Log.objects.create(
        visitor_id=visitor_id,
        log_action=log_action,
        ip_address=ip_address,
        additional_comments=kwargs.get('additional_comments', kwargs.get('comments', '')),
        device_info=kwargs.get('device_info', kwargs.get('device', '')),
        region=kwargs.get('region', ''),
        log_stat=kwargs.get('log_stat', kwargs.get('status', 'Successful !')),
    )
