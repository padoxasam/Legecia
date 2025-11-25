from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import AccessLog
from .serializers import AccessLogSerializer


class AccessLogListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        logs = AccessLog.objects.all()
        serializer = AccessLogSerializer(logs, many=True)
        return Response(serializer.data, status=200)
