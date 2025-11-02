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
    queryset=User.objects.all()
    serializer_class= RegisterSerializer
    permission_classes=[permissions.AllowAny]

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