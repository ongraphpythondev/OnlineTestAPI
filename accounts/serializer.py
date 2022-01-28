from dataclasses import fields
from django.forms import PasswordInput
from rest_framework import serializers
from accounts.models import CustomUser
from django.contrib.auth.hashers import make_password

# User Register Serializer for storing data using API.
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(RegisterUserSerializer,self).create(validated_data)
    
    class Meta:
        model = CustomUser
        fields = ['username','email','firstname','lastname','about','is_examiner','is_examinee','password']


# User Login Serializer for login in via API. (its just for simple login purpose.)
class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','password']


