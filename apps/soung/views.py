from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from apps.soung.models import (
    Soung,
    Album,
    Playlist
)

from apps.soung.serializers import (
    SoungCreateUpdateSerializer,
    SoungListSerializer,
    SoungRetrieveSerializer,

    AlbumCreateUpdateSerializer,
    AlbumListSerializer,
    AlbumRetrieveSerializer
)


class SoungAPIViewSet(ModelViewSet):
    queryset = Soung.objects.prefetch_related('artist').all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action in ('update', 'create'):
            return SoungCreateUpdateSerializer
        if self.action == 'list':
            return SoungListSerializer
        if self.action == 'retrieve':
            return SoungRetrieveSerializer
        return SoungListSerializer
        

class AlbumAPIViewSet(ModelViewSet):
    queryset = Album.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action in ('update', 'create'):
            return AlbumCreateUpdateSerializer
        if self.action == 'list':
            return AlbumListSerializer
        if self.action == 'retrieve':
            return AlbumRetrieveSerializer
        return AlbumListSerializer
