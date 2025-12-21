from django.shortcuts import render
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

from .models import Credentials
from .serializers import CredentialSerializer
from .services import hash_password, generate_salt, verify_password, generate_2fa_token
User=get_user_model()
class RegisterCredentialView(APIView):
    def post(self,request):
        serializer = CredentialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data.pop("password")
        salt = generate_salt()
        hashed = hash_password(password, salt)
        user=request.user
        if hasattr(user, "credentials"):
            return Response(
                {"error": "Credentials already exist for this user"},
                status=status.HTTP_400_BAD_REQUEST
            )
        Credentials.objects.create(
            user=user,                                        # ✅ ADD
            password_hashed=hashed,
            password_salt=salt,
            two_factor=False,
            two_factor_token=generate_2fa_token(),
            **serializer.validated_data)
        return Response({"message": "Credentials created"}, status=status.HTTP_201_CREATED)
class LoginCredentialView(APIView):
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        try:
            cred = Credentials.objects.get(username=username)
        except Credentials.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=400)

        if not verify_password(password, cred.password_hashed, cred.password_salt):
            cred.failed_entry += 1
            cred.save(update_fields=["failed_entry"])
           
            return Response({"error": "Invalid credentials"}, status=400)
        if cred.two_factor:
            return Response({'2fa_required':True,'token':cred.two_factor_token})
        
        cred.last_seen = timezone.now()
        cred.save(update_fields=["last_seen"])
        return Response({
            "access": str(RefreshToken.access_token),   
            "refresh": str(RefreshToken),                
            "role": cred.user.acive_role,         
            "username": cred.user.username
        })