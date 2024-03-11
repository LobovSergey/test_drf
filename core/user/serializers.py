from rest_framework import serializers
from .models import User
from organiztion.models import Organization


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        user.set_password(validated_data["password"])
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    organizations = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "email", "phone", "organizations"]
