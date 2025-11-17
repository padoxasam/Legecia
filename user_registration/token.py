from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
def email_token(user):
    domain='127.0.0.1:8000'
    uid64=urlsafe_base64_encode(force_bytes(user.pk))


    token=default_token_generator.make_token(user)
    link= f'http://{domain}/api/users/verify/{uid64}/{token}/'
    message=f'Welcome {user.username}\nClick HERE to verify Your Email\n{link}'
    send_mail("Verify Your Email",
        message,
        "no-reply@legecia.com",
        [user.email],
        fail_silently=False,)
    return link