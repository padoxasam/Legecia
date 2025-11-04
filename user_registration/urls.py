from django.urls import path
from .views import RegisterView , LoginView ,View ,UpdateInfo,VerifyEmail
urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(), name='login'),
    path('profile/',View.as_view() , name='Profile'),
    path('profile/update/',UpdateInfo.as_view(),name='Update'),
    path('verify-email/<uidb64>/<token>/',VerifyEmail.as_view(),name='verify_email'),
    
    
    
    ]



