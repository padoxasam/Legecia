from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Beneficiary, Guardian
from .serializers import (
    LoginSerializer,
    RoleSwitchSerializer,
    RegisterSerializer,
    UpdateProfileSerializer,
)
from .token import email_token

User = get_user_model()


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["u_email"]
        existing_user = User.objects.filter(u_email__iexact=email).first()

        if existing_user and existing_user.email_verified:
            return Response(
                {"error": "Account already exists and is verified"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if existing_user and not existing_user.email_verified:
            email_token(existing_user)
            return Response(
                {"success": True, "message": "Account exists but email not verified. Verification email resent."},
                status=status.HTTP_200_OK,
            )

        user = serializer.save()
        email_token(user)

        return Response(
            {"success": True, "message": "Registration successful. Please verify your email."},
            status=status.HTTP_201_CREATED,
        )


class ResendVerificationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"detail": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(u_email__iexact=email).first()
        if not user:
            return Response({"detail": "If the email exists, a verification link was sent."}, status=status.HTTP_200_OK)

        if user.email_verified:
            return Response({"detail": "Email already verified"}, status=status.HTTP_400_BAD_REQUEST)

        email_token(user)
        return Response({"detail": "Verification email sent"}, status=status.HTTP_200_OK)


class VerifyEmail(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uid64, token):
        try:
            uid = urlsafe_base64_decode(uid64).decode()
            user = User.objects.get(reg_id=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({"error": "Invalid link"}, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            user.email_verified = True
            user.save(update_fields=["email_verified"])
            return Response({"message": "Email verified successfully"})

        return Response({"message": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        if not user.email_verified:
            return Response(
                {"error": "Please verify your email before login"},
                status=status.HTTP_403_FORBIDDEN,
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "message": "Login successful",
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
                "user": {
                    "id": user.reg_id,
                    "username": user.u_username,
                    "email": user.u_email,
                    "email_verified": user.email_verified,
                    "active_role": user.active_role,
                },
            },
            status=status.HTTP_200_OK,
        )


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.reg_id,
            "username": user.u_username,
            "email": user.u_email,
            "email_verified": user.email_verified,
            "active_role": user.active_role,
        })


class UpdateInfo(generics.UpdateAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user


class SwitchRoleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RoleSwitchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_role = serializer.validated_data["role"]
        user = request.user

        if new_role == "USER":
            user.active_role = "USER"
            user.save(update_fields=["active_role"])
            return Response({"message": "Switched to USER role", "active_role": "USER"})

        if new_role == "BENEFICIARY":
            if not Beneficiary.objects.filter(user_id=user).exists():
                return Response({"error": "Beneficiary profile not found"}, status=status.HTTP_403_FORBIDDEN)

        if new_role == "GUARDIAN":
            if not Guardian.objects.filter(user_id=user).exists():
                return Response({"error": "Guardian profile not found"}, status=status.HTTP_403_FORBIDDEN)

        user.active_role = new_role
        user.save(update_fields=["active_role"])
        return Response({"message": "Role switched successfully", "active_role": new_role})
