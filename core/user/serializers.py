from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        exclude = ("password",)
