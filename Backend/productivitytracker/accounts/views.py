from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import Profile_Serializer
from .models import Profile
# to generate tokens each time a user logs in
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Create your views here.
class ProfileView(generics.CreateAPIView):
    '''reading the objects from the Profile class, 
    referring to the serializer fro the accounts, 
    modifying permissions and allowing any '''
    query_set = Profile.objects.all()
    serializer_class = Profile_Serializer
    permissions = [permissions.AllowAny]

class CustomTokenobtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        return token 
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = Profile_Serializer