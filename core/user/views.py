from rest_framework import generics, mixins, permissions, viewsets
from .models import User
from .serializers import UserSerializer, UserRegisterSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    model = User
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserRetrieveOptionsAPIViewSet(mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
