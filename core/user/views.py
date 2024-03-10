from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import response
from .models import User
from .serializers import UserSerializer, UserRegisterSerializer


class UserViewSet(viewsets.ExceptListViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
