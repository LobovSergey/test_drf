from django.shortcuts import render
from rest_framework import viewsets, response
from .models import Event
from .serializer import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

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
