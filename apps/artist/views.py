from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from apps.artist.models import Artist
from apps.artist.serializers import (
    ArtistSerializer
)


class ArtistAPIViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ArtistSerializer
