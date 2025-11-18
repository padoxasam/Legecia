from django.urls import path 
from .views import CommunicationView , CommuncationvViewList
urlpatterns = [path('Communication/create/',CommunicationView.as_view(),name='Create-Communication'),
               path('Communication/all/',CommuncationvViewList.as_view(),name='All-Communication'
                   
               ),
               
               
               ]