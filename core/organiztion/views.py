from rest_framework import viewsets, permissions

from .models import Organization
from .serializer import OrganizationSerializer


class OrganizationCreateAPI(viewsets.ReadOrCreateViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
