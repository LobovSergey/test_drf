from rest_framework import generics, viewsets
from .models import User
from .serializers import UserSerializer, UserRegisterSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UserRetrieveOptionsAPIViewSet(viewsets.RUDViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
