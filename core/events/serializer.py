from rest_framework import serializers
from organiztion.models import Organization


from .models import Event


class EventSerializer(serializers.ModelSerializer):
    organizations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Organization.objects.all())

    class Meta:
        model = Event
        fields = "__all__"
