from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import Credentials
from .serializers import CredentialSerializer

class CredentialAdminListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        creds = Credentials.objects.all()
        serializer = CredentialSerializer(creds, many=True)
        return Response(serializer.data)
