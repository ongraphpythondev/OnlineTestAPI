from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from accounts.models import CustomUser
from accounts.serializer import RegisterUserSerializer , LoginUserSerializer
from django.contrib.auth import authenticate ,login ,logout


# Create your views here.

# Registering User 
class RegisterAPIView(ViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterUserSerializer
    
    def create(self,request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

# User Login API for logging in . 
class LoginAPIView(ViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = LoginUserSerializer
    
    
    def create(self,request):
        user = authenticate(request, username=request.data['username'],password=request.data['password'])
        if user is not None :
            login(request,user)
            return Response({"Logged in": "User Logged in"},status=status.HTTP_200_OK)
        else:
            return Response({"Access denied": "User credential are incorrect"},status=status.HTTP_400_BAD_REQUEST)

# Logout API , just a simple url for user logging out .
class LogoutAPIView(ViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = LoginUserSerializer
    
    def list(self,request):
        logout(request)
        return Response({"Logging out": "User Logged out."},status=status.HTTP_200_OK)