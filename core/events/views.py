from rest_framework import viewsets, response, permissions, status
from .models import Event
from .serializer import EventSerializer
from .tools import *
from django.shortcuts import render


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Event.objects.all()

        title = self.request.query_params.get("title")
        ordering = self.request.query_params.get("ord_date")
        date_day = self.request.query_params.get("day")
        date_month = self.request.query_params.get("month")
        date_year = self.request.query_params.get("year")

        if ordering:
            queryset = queryset.order_by("-date")
        if date_day:
            queryset = queryset.filter(title__icontains=title)
        if date_day:
            queryset = queryset.filter(date__day=date_day)
        if date_month:
            queryset = queryset.filter(date__month=date_month)
        if date_year:
            queryset = queryset.filter(date__year=date_year)
        return queryset

    def create(self, request, *args, **kwargs):
        ip = request.META.get("REMOTE_ADDR")
        accept = access_ip(ip)
        if accept:
            return super().create(request, *args, **kwargs)
        return response.Response(
            data='{"error": "service timeout"}', status=status.HTTP_423_LOCKED
        )

    def retrieve(self, request, *args, **kwargs):
        data = request
        return render(request=request, template_name="event_retrieve.html")
