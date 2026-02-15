from django.urls import path
from .views import CommunicationCreateView, CommunicationListView

urlpatterns = [
    path('create/', CommunicationCreateView.as_view(), name='create-communication'),
    path('all/', CommunicationListView.as_view(), name='all-communication'),
]
