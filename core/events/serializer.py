from rest_framework import serializers

from organiztion.serializer import OrganizationSerializer
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    organizations = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Event
        fields = "__all__"
