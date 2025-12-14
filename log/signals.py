from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from .services import create_log
from django.db.models.signals import post_save
from package.models import Package

def get_visitor_type(user):
    if hasattr(user, 'active_role'):
        if user.active_role == 'BENEFICIARY':
            return 'Beneficiary'
        elif user.active_role == 'GUARDIAN':
            return 'Guardian'
    return 'User'


@receiver(user_logged_in)
def log_user_login(sender, user, request, **kwargs):
    create_log(
        visitor_type=get_visitor_type(user),
        visitor_id=user.id,
        log_action='LOGIN_SUCCESS',
        ip_address=request.META.get('REMOTE_ADDR'),
        additional_comments='User logged in successfully',
        device_info=request.META.get('HTTP_USER_AGENT', ''),
        region=request.headers.get('X-Region')
    )


@receiver(user_login_failed)
def log_failed_login(sender, credentials, request, **kwargs):
    username = credentials.get('username') or credentials.get('email')

    create_log(
        visitor_type='User',
        visitor_id=0,
        log_action='LOGIN_FAILED',
        ip_address=request.META.get('REMOTE_ADDR'),
        additional_comments=f'Failed login attempt for {username}',
        device_info=request.META.get('HTTP_USER_AGENT', ''),
        region=request.headers.get('X-Region')
    )


@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    create_log(
        visitor_type=get_visitor_type(user),
        visitor_id=user.id,
        log_action='LOGOUT',
        ip_address=request.META.get('REMOTE_ADDR'),
        additional_comments='User logged out',
        device_info=request.META.get('HTTP_USER_AGENT', ''),
        region=request.headers.get('X-Region')
    )


@receiver(post_save, sender=Package)
def log_package_create(sender, instance, created, **kwargs):
    if not created:
        return

    owner = instance.owner
    create_log(
        visitor_type=get_visitor_type(owner),
        visitor_id=owner.id,
        log_action='PACKAGE_CREATED',
        ip_address='0.0.0.0',
        additional_comments=f"Package '{instance.pack_name}' created",
        device_info='System'
    )
