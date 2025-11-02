from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
User= get_user_model()
class RegisterView(generics.CreateAPIView):
    query=User.objects.all()
    serializer_class= RegisterSerializer
    permission=[permissions.AllowAny]

class LoginView(generics.GenericAPIView):
    permission_class= [permissions.AllowAny]

    def post(self, request):
        username=request.data.get('username')
        password= request.data.get('password')
        user = authenticate(username=username,password=password)
        if not user: 
            return Response ( {'Error': 'Invalid Credentials ❌'}
                             , status=status.HTTP_400_Bad_Request)
        
        refresh=RefreshToken.for_user(user)
        return Response ( {'Refresh' : str(refresh),
                           'Access'  : str(refresh.access_token),
                           'user'    : {'username':user.username,'email':user.email}
                           })