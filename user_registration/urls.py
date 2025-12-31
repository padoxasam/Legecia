from django.urls import path
from .views import RegisterView , ResendVerificationView ,  LoginView ,ProfileView ,UpdateInfo,VerifyEmail,SwitchRoleView
urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(), name='login'),
    path('profile/',ProfileView.as_view() , name='Profile'),
    path('profile/update/',UpdateInfo.as_view(),name='Update'),
    path('verify-email/<uid64>/<token>/', VerifyEmail.as_view()),
    path('switch-role/',SwitchRoleView.as_view(),name=' Switch role '),
    path("resend-verification/", ResendVerificationView.as_view()),
 
    ]



