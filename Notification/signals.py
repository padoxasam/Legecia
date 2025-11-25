from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from user_registration.models import Beneficiary,Guardian,User
from supervised.models import SupervisedPack
from package.models import Package
from .services import create_notification
User=get_user_model()
@receiver(post_save,sender=User)
def notify_account_created(sender,instance,created,**kwargs):
    if created:
        create_notification(sender_id=instance.id,
                            receiver_id=instance.id,
                            visitor_type='user_info',
                            topic='Welcome to LEGECIA !',
                message='Your Account Has Been Successfully Created Ya 3m !\nWelcome Onboard !'),
        
        priority='Medium',
@receiver(post_save,sender=Package)
def notify_package_created(sender,instance,created,**kwargs):
    if created:
        owner=instance.owner
        create_notification(
            sender_id=owner.id,receiver_id=owner.id,
            visitor_type='user_info',topic='Package Created',
            message=f'Your Package ({instance.pack_name}) was created Successfully ! ',
            priority='Medium',

        )
@receiver(post_save,sender=SupervisedPack)
def guardian_supervisison_noti(sender,instance,created,**kwargs):
    if created:
        guardian=instance.guard
        package=instance.pack
        user=instance.user
        create_notification(sender=guardian.id,receiver_id=guardian.id,visitor_type='Guardian',topic='New Supervised Package Has been created :{instance.pack_name}/nBy{self.u_full_name}',message='You have been Assigned over {Package.pack_name}',
                            priority='High',)
@receiver(post_save,sender=Beneficiary)
def bene_up_noti(sender,instance,created,**kwargs):
    if not created:
        create_notification(sender_id=instance.id,receiver_id=instance.branch_id,visitor_type='Beneficiary',
                            topic='Milestone Update',
                            message=f'beneficiary{instance.b_full_name} Uploaded a Milestone !',priority='High')