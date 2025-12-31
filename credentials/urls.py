# credentials/urls.py
from django.urls import path
from .views import RegisterCredentialView, LoginCredentialView

urlpatterns = [
    path("register/", RegisterCredentialView.as_view(), name="create_credentials"),
    path("login/", LoginCredentialView.as_view(), name="login_credentials"),
]
