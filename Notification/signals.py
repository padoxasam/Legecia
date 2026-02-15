from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from user_registration.models import Beneficiary, Guardian
from supervised.models import SupervisedPack
from package.models import Package
from .services import create_notification

User = get_user_model()


@receiver(post_save, sender=User)
def notify_account_created(sender, instance, created, **kwargs):
    if created:
        create_notification(
            sender_id=instance.reg_id,
            receiver_id=instance.reg_id,
            visitor_type='User',
            topic='Welcome to LEGECIA!',
            message='Your Account Has Been Successfully Created!',
            priority='Medium',
        )


@receiver(post_save, sender=Package)
def notify_package_created(sender, instance, created, **kwargs):
    if created:
        owner_id = instance.owner
        create_notification(
            sender_id=owner_id,
            receiver_id=owner_id,
            visitor_type='User',
            topic='Package Created',
            message=f'Your Package ({instance.pack_name}) was created successfully!',
            priority='Medium',
        )


@receiver(post_save, sender=SupervisedPack)
def guardian_supervision_noti(sender, instance, created, **kwargs):
    if created:
        guardian = instance.guard
        package = instance.pack
        user = instance.user
        create_notification(
            sender_id=user.reg_id,
            receiver_id=guardian.user_id_id,
            visitor_type='Guardian',
            topic='New Supervised Package',
            message=f'You have been assigned to supervise {package.pack_name}',
            priority='High',
        )


@receiver(post_save, sender=Beneficiary)
def bene_up_noti(sender, instance, created, **kwargs):
    if not created:
        create_notification(
            sender_id=instance.user_id_id,
            receiver_id=instance.user_id_id,
            visitor_type='Beneficiary',
            topic='Profile Updated',
            message='Beneficiary profile updated successfully',
            priority='Medium',
        )
