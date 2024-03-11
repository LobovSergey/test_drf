from rest_framework import generics, viewsets
from .models import User
from .serializers import UserSerializer, UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status


class UserRegisterAPIView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = UserRegisterSerializer


class UserRetrieveOptionsAPIViewSet(viewsets.RUDViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
