from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from apps.soung.models import (
    Soung,
    Album,
    Playlist
)

from django_filters.rest_framework import DjangoFilterBackend

from utils.permissions import IsMyPlaylist

from apps.soung.serializers import (
    SoungCreateUpdateSerializer,
    SoungListSerializer,
    SoungRetrieveSerializer,

    AlbumCreateUpdateSerializer,
    AlbumListSerializer,
    AlbumRetrieveSerializer,

    PlaylistSeralizer,
    PlayCreateUpdatelistSeralizer
)


class SoungAPIViewSet(ModelViewSet):
    queryset = Soung.objects.prefetch_related('artist').all()
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genres', 'artist']

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


class PlaylistAPIViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    permission_classes = [IsMyPlaylist]
    serializer_class = PlaylistSeralizer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return PlayCreateUpdatelistSeralizer
        return PlaylistSeralizer
    
    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)