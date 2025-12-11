from django.urls import path
from .views import RegisterView , LoginView ,View ,UpdateInfo,VerifyEmail,SwitchRoleView
urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(), name='login'),
    path('profile/',View.as_view() , name='Profile'),
    path('profile/update/',UpdateInfo.as_view(),name='Update'),
    path('verify-email/<uidb64>/<token>/',VerifyEmail.as_view(),name='verify_email'),
    path('switch-role/',SwitchRoleView.as_view(),name=' Switch role ')
     
    ]



