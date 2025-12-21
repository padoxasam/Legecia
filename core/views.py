from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CoreProfile
from .serializers import CoreProfileSerializer

from user_registration.permissions import IsUserRole,IsBeneficiaryRole,IsGuardianRole



class CoreProfileView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile, _ = CoreProfile.objects.get_or_create(user=request.user)
        return Response(CoreProfileSerializer(profile).data)

    def put(self, request):
        profile, _ = CoreProfile.objects.get_or_create(user=request.user)
        serializer = CoreProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
class UserDashboardView(APIView):
    """
    USER dashboard
    """
    permission_classes = [IsAuthenticated, IsUserRole]

    def get(self, request):
        return Response({
            'dashboard': 'USER',
            'actions': [
                'create_package',
                'view_packages',
                'add_beneficiary',
                'assign_guardian',
            ]
        })


class BeneficiaryDashboardView(APIView):
    """
    BENEFICIARY dashboard
    """
    permission_classes = [IsAuthenticated, IsBeneficiaryRole]

    def get(self, request):
        return Response({
            'dashboard': 'BENEFICIARY',
            'actions': [
                'view_received_packages',
                'view_guardian_info',
            ]
        })


class GuardianDashboardView(APIView):
    """
    GUARDIAN dashboard
    """
    permission_classes = [IsAuthenticated, IsGuardianRole]

    def get(self, request):
        return Response({
            'dashboard': 'GUARDIAN',
            'actions': [
                'view_supervised_packages',
                'approve_access',
                'release_access',
            ]
        })
