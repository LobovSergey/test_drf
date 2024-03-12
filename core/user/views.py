from rest_framework import generics, viewsets, permissions
from .models import User
from .serializers import UserSerializer, UserRegisterSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    model = User
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserRetrieveOptionsAPIViewSet(viewsets.RUDViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
