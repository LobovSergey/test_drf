from rest_framework import viewsets, response, permissions, status
from .models import Event
from .serializer import EventSerializer
from .tools import *


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Event.objects.all()
        title = self.request.query_params.get('title')
        ordering = self.request.query_params.get('ord')
        if title is not None:
            queryset = queryset.filter(title=title)
        if ordering:
            print(ordering)
            queryset = queryset.order_by("date")
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = EventSerializer(request.data)
        ip = request.META.get('REMOTE_ADDR')
        accept, time = access_ip(ip)
        if accept:
            return super().create(request, *args, **kwargs)
        return response.Response(data='{"error": "service timeout"}', status=status.HTTP_423_LOCKED)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
