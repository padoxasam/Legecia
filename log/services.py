from .models import Log
def create_log(user, log_action, ip_address, **kwargs):
    Log.objects.create(
        user=user,
        log_action=log_action,
        ip_address=ip_address,
        additional_comments=kwargs.get('comments'),
        device_info=kwargs.get('device'),
        region=kwargs.get('region'),
        log_stat=kwargs.get('status', 'Successful !')
    )
