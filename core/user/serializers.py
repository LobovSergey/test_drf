from rest_framework import serializers
from .models import User
from organiztion.models import Organization


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]


class UserSerializer(serializers.ModelSerializer):
    organizations = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "email", "phone", "organizations"]
