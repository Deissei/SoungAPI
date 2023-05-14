from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from apps.artist.models import Artist
from apps.artist.serializers import (
    ArtistSerializer,
    ArtistCreateUpdateSerializer
)


class ArtistAPIViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return ArtistCreateUpdateSerializer
        return ArtistSerializer
