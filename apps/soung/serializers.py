from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from apps.soung.models import (
    Soung,
    Album,
    Playlist
)
from apps.artist.serializers import ArtistSerializer
from apps.soung.models import Soung

from rest_framework import serializers


class SoungListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soung
        fields = ('title', 'file', 'image')


class SoungCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soung
        fields = ('title', 'artist', 'file', 'image')


class SoungRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soung
        fields = (
            'id',
            'title',
            'artist',
            'image',
            'file',
            'url'
        )


class AlbumListSerializer(serializers.ModelSerializer):
    soungs = SoungListSerializer(many=True)
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = (
            'title',
            'soungs',
            'artist',
        )


class AlbumRetrieveSerializer(serializers.ModelSerializer):
    soungs = SoungRetrieveSerializer(many=True)
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = (
            'id',
            'title',
            'description',
            'soungs',
            'artist',
            'url'
        )


class AlbumCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = (
            'title',
            'description',
            'soungs',
            'artist',
        )


class PlaylistSeralizer(serializers.ModelSerializer):
    user = serializers.SlugField(read_only=True)
    soungs = SoungRetrieveSerializer(many=True)

    class Meta:
        model = Playlist
        fields = (
            'id',
            'user',
            'title',
            'soungs'
        )


class PlayCreateUpdatelistSeralizer(serializers.ModelSerializer):
    user = serializers.SlugField(read_only=True)

    class Meta:
        model = Playlist
        fields = (
            'id',
            'user',
            'title',
            'soungs'
        )