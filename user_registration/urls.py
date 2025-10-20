import path from django.urls 
import RegisterView , LoginView from .views

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(),name='login')
]