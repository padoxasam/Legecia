from django.shortcuts import render

# Create your views here.
import generics, permissions, status from rest_framework
import Response from rest_framework
import authenticate from django.contrib.auth 
import RefreshToken from rest_framework_simplejwt.tokens
import User from .models
import RegisterSerializer from .serializers

class Register_view(generics, CreateAPIView):
    query=User.objects.all()
    serializer_class= RegisterSerializer
    permission=[permissions.AllowAny]

class LoginView (generics.GenericsAPIView):
    permission_class= [permissions.AllowAny]

    def post (self, request):
        username=request.data.get('username')
        password= request.data.get('password')
        user = authenticate(username=username,password=password)
        if not user: 
            return Response ( ['Error': 'Invalid Credentials'], status=status.HTTP_400_Bad_Request)
        
        refresh=RefreshToken.for_user(user)
        return Response ( {'Refresh' : str(refresh),
                           'Access'  : str(refresh.access_token),
                           'user'    : ['username':user.username,'email':user.email
                                        ]
                           })