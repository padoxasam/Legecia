from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import authenticate,get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from .token import email_token 
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from rest_framework.views import APIView
from django.db import connection

from .serializers import LoginSerializer,RoleSwitchSerializer
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
    def get(self,request,uid64,token):
        try :
            uid=urlsafe_base64_decode(uid64).decode()
            user=User.objects.get(pk=uid)
        except( TypeError,ValueError,OverflowError,User.DoesNotExist):
            return Response({'Error':'Invalid Link'},status=400)
        if default_token_generator.check_token(user,token):
            user.is_verified=True
            user.save()
            return Response({'Message':'Email Verified Successfully'})
        else:
            return Response ({'Message':'Invalid or Exiperd Token'},status=400)    
class LoginView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    permission_classes= [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        refresh=RefreshToken.for_user(user)
        return Response({'Message': 'Login Successful !',
                        'access_token' : str(refresh.access_token),
                        'refresh_token': str(refresh),
                        'user': {'username': user.username,
                                 'email' : user.email,
                                 'full_name':user.full_name
                                 }

        },status=status.HTTP_200_OK)
    
       
class View(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated] 
    def get(self,request,*args,**kwargs):
        user=request.user
        return Response({'id':user.id,
            'username':user.username,
                         'email': user.email,
                            'id': user.id

        })  
class UpdateInfo(generics.UpdateAPIView):
    permission_classes=[IsAuthenticated]
    def put(self,request,*args,**kwargs):
        user=request.user
        user.username=request.data.get('username',user.username)
        user.email=request.data.get('email',user.email)
        user.save()
        return Response ({'Message':"Profile Updated Successfully !"} )
class SwitchRoleView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=RoleSwitchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_role=serializer.validated_data['role']
        user=request.user
        has_role=False
        username=user.username
        with connection.cursor() as cursor:
            if new_role=='USER':
                has_role=True
            elif new_role=='BENEFICIARY':
                cursor.execute('SELECT 1 FROM beneficiary WHERE b_username = %s',[username])
                has_role=cursor.fetchone() is not None
            elif new_role=='GUARDIAN':
                cursor.execute('select 1 from guardian_info where g_username= %s',[username])
                has_role=cursor.fetchone() is not None
        if not has_role:
            return Response({'Error':f"You Dont't have a {new_role} profile !"},status=403)
        user.active_role=new_role
        user.save()
        return Response({'Message':'Role Switched Successfully !',
                        'active_role':new_role})