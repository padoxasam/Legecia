from django.urls import path 
from .views import MarkAsSeenAPI,NotificationDetailAPI,NotificationListAPI
urlpatterns=[
    path('list',NotificationListAPI.as_view(),name='Notification List'),
    path('<int:noti_id>/',NotificationDetailAPI.as_view(),name='Notification Detail'),
    path('mark/<int:noti_id>/',MarkAsSeenAPI.as_view(),name='Mark as Read'),
    ]