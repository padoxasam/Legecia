from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.utils import timezone

from log.models import Log
from .services import create_access_log, close_access_log
@receiver(user_logged_in)
def access_log_login(sender,user,request,**kwargs):
    ip=request.META.get('REMOTE_ADDR')
    device=request.META.get('HTTO_USER_AGENT')
    try:
        latest_log=Log.objects.filter(visitor_id=user.id).latest('log_at')
    except Log.DoesNotExist:
        latest_log=None
    request.session["access_log_id"] = create_access_log(
        ip_address=ip,
        device_info=device,
        log=latest_log,
        successful=True,
    ).access_id
@receiver(user_logged_out)
def access_log_logout(sender, user, request, **kwargs):
    log_id = request.session.get("access_log_id")
    if not log_id:
        return

    from .models import AccessLog
    try:
        entry = AccessLog.objects.get(access_id=log_id)
        close_access_log(entry)
    except AccessLog.DoesNotExist:
        pass
receiver(user_login_failed)
def access_log_failed(sender, credentials, request, **kwargs):
    ip = request.META.get("REMOTE_ADDR", "0.0.0.0")
    device = request.META.get("HTTP_USER_AGENT", "")

    username = credentials.get("username") or credentials.get("email")

    create_access_log(
        ip_address=ip,
        device_info=device,
        log=None,
        successful=False,
        failure_message=f"Failed login attempt for: {username}",)