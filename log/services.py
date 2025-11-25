from .models import Log

def create_log(visitor_type,visitor_id,log_action,ip,device=None,region=None,comments=None,status='successful !'):
    Log.objects.create(visitor_type=visitor_type,
                       visitor_id=visitor_id,
                       log_action=log_action,ip_address=ip,
                       device_info=device,region=region,
                       additional_comments=comments,
                       log_stat=status,
    )
