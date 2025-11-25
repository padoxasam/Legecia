from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from .services import create_log
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import Log
from package.models import Package
User=get_user_model()



def get_visitor_type(user):
    if hasattr(user,'account_type'):
        if user.account_type=='BENEFICIARY':
            return 'Beneficairy'
        elif user.account_type=='GUARDIAN':
            return 'Guardian'
        else:
            return 'User'
    return 'User'


@receiver(user_logged_in)
def log_user_login(sender,user,request,**kwargs):
    create_log(visitor_type=get_visitor_type(user),
               visitor_id=user.id,
               ip_address=request.META.get('REMOTE_ADDR'),
               log_action='Login Successful !',
               additional_comments='User Logged in Successfully !',
               device_info=request.META.get('HTTP_USER_AGENT',''),
               region=request.headers.get('X-Region',None),
    )
@receiver(user_login_failed)
def log_failed_login(sender,credentials,reqeust,**kwargs):
    username=credentials.get('username') or credentials.get('email')

    create_log(visitor_type='User',visitor_id=0,ip_address=reqeust.META.get('REMOTE_ADDR'),
               log_action='Login Failed',
               additional_comments=f'Failed Login attempt for username:{username}',
               device_info=reqeust.META.get('HTTP_USER_AGENT',''),
               region=reqeust.headers.get('X-Region',None),
               
               )
@receiver(user_logged_out)
def log_logout(sender,request,user,**kwargs):
    create_log(visitor_type=get_visitor_type(user),
               visitor_id=user.id ,
               ip_address=request.META.get('REMOTE_ADDR'),
               log_action='LOG OUT',
               additional_comments='User logged out',
               device_info=request.META.get('HTTP_USER_AGENT',''),
               region=request.headers.get('X-Region',None),
               
               )
@receiver(post_save,sender=Package)
def log_package_create(sender,instance,created,**kwargs):
    if not created:
        return
    owner=instance.owner
    create_log(visitor_type=get_visitor_type(owner),
               visitor_id=owner.id,
               ip_Address='0.0.0.0',
               log_action='Package Created',
               additonal_comments=f"Package'{instance.pack_name}' created",
               device_info='System',
               region=None,
               )