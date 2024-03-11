from rest_framework import generics, viewsets
from .models import User
from .serializers import UserSerializer, UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status


class UserRegisterAPIView(generics.CreateAPIView):
    model = User
    serializer_class = UserRegisterSerializer


class UserRetrieveOptionsAPIViewSet(viewsets.RUDViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
