from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import Log
from .serializers import LogSerializer

class LogListView(APIView):
    permission_classes=[IsAdminUser]

    def get(self,request):
        logs=Log.objects.all().order_by('-log_at')
        serializer=LogSerializer(logs,many=True)
        return Response(serializer.data)
    