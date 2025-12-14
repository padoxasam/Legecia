from rest_framework import generics
from .models import CommunicationMeans
from .serializer import CommunicationSerializer


class CommunicationCreateView(generics.CreateAPIView):
    queryset = CommunicationMeans.objects.all()
    serializer_class = CommunicationSerializer


class CommunicationListView(generics.ListAPIView):
    queryset = CommunicationMeans.objects.all()
    serializer_class = CommunicationSerializer
