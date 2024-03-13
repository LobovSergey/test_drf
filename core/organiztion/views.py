from rest_framework import mixins, permissions, viewsets

from .models import Organization
from .serializer import OrganizationSerializer


class OrganizationCreateAPI(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
