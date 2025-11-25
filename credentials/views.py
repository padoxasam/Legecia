from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Credenntials
from .serializers import CredentialSerializer
from .services import hash_password, generate_salt, verify_password, generate_2fa_token
class RegisterCredentialView(APIView):
    def post(self,request):
        serializer = CredentialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = request.data["password"]
        salt = generate_salt()
        hashed = hash_password(password, salt)
        cred = Credenntials.objects.create(
            username=request.data["username"],
            password_hashed=hashed,
            password_salt=salt,
            security_qu1=request.data["security_qu1"],
            security_ans1=request.data["security_ans1"],
            security_qu2=request.data["security_qu2"],
            security_ans2=request.data["security_ans2"],
            recovery_email=request.data["recovery_email"],
            two_factor=False,
            two_factor_token=generate_2fa_token(),
        )
        return Response({"message": "Credentials created"}, status=status.HTTP_201_CREATED)
class LoginCredemtialView(APIView):
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        try:
            cred = Credential.objects.get(username=username)
        except Credential.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=400)

        if not verify_password(password, cred.password_hashed, cred.password_salt):
            cred.failed_entry += 1
            cred.save(update_fields=["failed_entry"])
            return Response({"error": "Invalid credentials"}, status=400)

        if cred.two_factor:
            return Response({"2fa_required": True, "token": cred.two_factor_token})
        return Response({"login": "success"})