from django.shortcuts import render
from rest_framework import viewsets

from .models import Organization
from .serializer import OrganizationSerializer


class OrganizationCreateAPI(viewsets.ReadOrCreateViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
