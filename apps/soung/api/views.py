from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from apps.soung.models import Album, Playlist, Soung
from apps.soung.api.serializers import (AlbumCreateUpdateSerializer,
                                    AlbumSerializer,
                                    PlaylistCreateUpdateSerializer,
                                    PlaylistSerializer,
                                    SoungCreateUpdateSerializer,
                                    SoungSerializer)
from utils.permissions import IsMyPlaylist


class SoungAPIViewSet(ModelViewSet):
    queryset = Soung.objects.prefetch_related('artist').all()
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['genres', 'artist']
    search_fields = ['title']

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return SoungCreateUpdateSerializer
        return SoungSerializer        


class AlbumAPIViewSet(ModelViewSet):
    queryset = Album.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return AlbumCreateUpdateSerializer
        return AlbumSerializer


class PlaylistAPIViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    permission_classes = [IsMyPlaylist]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return PlaylistCreateUpdateSerializer
        return PlaylistSerializer
