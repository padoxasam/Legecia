from .models import AccessLog
from django.utils import timezone

def create_access_log(ip_address,device_info='',log='',successful=True,failure_message=None,):
    return AccessLog.objects.create(ip_address=ip_address,device_info=device_info,log=log,successful_log=successful,failure_message=failure_message,login_start=timezone.now())
def close_access_log(log_entry):
    log_entry.logout=timezone.now()
    log_entry.save()
    return log_entry