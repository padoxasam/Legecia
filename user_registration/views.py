from django.shortcuts import render

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import authenticate,get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User,Beneficiary,Guardian
from rest_framework.permissions import IsAuthenticated
from .token import email_token 
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from rest_framework.views import APIView
from .serializers import LoginSerializer,RoleSwitchSerializer,RegisterSerializer,UpdateProfileSerializer
User= get_user_model()
class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class= RegisterSerializer
    permission_classes=[permissions.AllowAny]
    def perform_create(self, serializer):
        user=serializer.save()
        email_token(user)
        return user
class VerifyEmail(APIView):
    permission_classes=[permissions.AllowAny]
    def get(self,request,uid64,token):
        try :
            uid=urlsafe_base64_decode(uid64).decode()
            user=User.objects.get(pk=uid)
        except( TypeError,ValueError,OverflowError,User.DoesNotExist):
            return Response({'Error':'Invalid Link'},status=400)
        if default_token_generator.check_token(user,token):
            user.email_verified=True
            user.save(update_fields=['email_verified'])
            return Response({'Message':'Email Verified Successfully'})
        else:
            return Response ({'Message':'Invalid or Exiperd Token'},status=400)  
          
class LoginView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    permission_classes= [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        if not user.email_verified:
           
            return Response(
                {'error': 'Please verify your email before login'},
                status=status.HTTP_403_FORBIDDEN
            )

        refresh=RefreshToken.for_user(user)
        return Response({'Message': 'Login Successful !',
                        'access_token' : str(refresh.access_token),
                        'refresh_token': str(refresh),
                        'user': {'id': user.id,
                                 'email' : user.email,
                                 'active_role': user.active_role
                                 }

        },status=status.HTTP_200_OK)
    
       
class ProfileView(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated] 
    def get(self,request):
        user=request.user
        return Response({'id':user.id,
            'username':user.username,
                         'email': user.email,
                         'email_verified':user.email_verified,
                         'active_role':user.active_role
                            

        })  
class UpdateInfo(generics.UpdateAPIView):
    serializer_class=UpdateProfileSerializer
    permission_classes=[IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return self.request.user
        
        
    
class SwitchRoleView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=RoleSwitchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        new_role=serializer.validated_data['role']
        user=request.user
        if new_role == 'USER':
            user.active_role = 'USER'
            user.save(update_fields=['active_role'])
            return Response({'message': 'Switched to USER role'})

        if new_role == 'BENEFICIARY':
            if not Beneficiary.objects.filter(user_id=user.id).exists():
                return Response({'error': 'Beneficiary profile not found'}, status=403)
        if new_role == 'GUARDIAN':
            if not Guardian.objects.filter(user_id=user.id).exists():
                return Response({'error': 'Guardian profile not found'}, status=403)

        
        
        user.active_role=new_role
        user.save(update_fields=['active_role'])
        return Response({
            'message': 'Role switched successfully',
            'active_role': new_role
        })

    