from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
def email_token(user):
    token=default_token_generator.make_token(user)
    user_id=urlsafe_base64_encode(force_bytes(user.pk))
    verify_url=f'http://{domain}/api/users/verify_email/{user_id}/{token}'
    topic='Verify your Legecia account Now !'
    pop=f'Deer {user.username},Please Verify Your account Using this LiNK{verify_url}'
    send_mail(topic,pop,settings.DEFAULT_FROM_EMAIL,[user.email])