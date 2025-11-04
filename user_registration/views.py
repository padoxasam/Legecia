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

User= get_user_model()
class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class= RegisterSerializer
    permission_classes=[permissions.AllowAny]
    def crite(self, serializer):
    
        user=serializer.save()
        email_token(user)
        return user
class VerifyEmail(APIView):
    def get(self,uid64,token):
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
    permission_classes= [permissions.AllowAny]

    def post(self, request):
        username=request.data.get('username')
        password= request.data.get('password')
        if not username or not password:
            return Response({'Error': 'Please Provide Both username And password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username,password=password)
        if not user: 
            return Response ( {'Error': 'Invalid Credentials ❌'}
                             , status=status.HTTP_400_BAD_REQUEST)
        
        refresh=RefreshToken.for_user(user)
        return Response ( { 'Message' : 'Login Successful !',
                            'Refresh' : str(refresh),
                           'Access'  : str(refresh.access_token),
                           'user'    : {'username':user.username,'email':user.email}
                           }, status=status.HTTP_200_OK)
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
    