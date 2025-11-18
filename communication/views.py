from django.shortcuts import render

# Create your views here.
from rest_framework import generics 
from .models import communicationMeans
from .serializer import CommunicationSerializer
class CommunicationView(generics.CreateAPIView):
    queryset=communicationMeans.objects.all()
    serializer_class=CommunicationSerializer

class CommuncationvViewList(generics.ListAPIView):
    queryset=communicationMeans.objects.all()
    serializer_class=CommunicationSerializer
    