from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Log
from .serializers import LogSerializer


class LogListView(generics.ListAPIView):
    
    queryset = Log.objects.all().order_by('-log_at')
    serializer_class = LogSerializer
    permission_classes = [IsAdminUser]


class MyLogListView(generics.ListAPIView):
    
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Log.objects.filter(
            visitor_id=self.request.user.id
        ).order_by('-log_at')
