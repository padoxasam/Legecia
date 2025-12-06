# credentials/urls.py
from django.urls import path
from .views import RegisterCredentialView, LoginCredemtialView

urlpatterns = [
    path("register/", RegisterCredentialView.as_view(), name="create_credentials"),
    path("login/", LoginCredemtialView.as_view(), name="login_credentials"),
]
