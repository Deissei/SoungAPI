from rest_framework import serializers

from apps.artist.serializers import ArtistSerializer
from apps.genre.serializers import GenreSerializer
from apps.soung.models import Album, Playlist, Soung


# Сериалайзер для Песен
class SoungSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    artist = ArtistSerializer(read_only=True)
    class Meta:
        model = Soung
        fields = (
            'id',
            'title',
            'artist',
            'image',
            'genres',
            'file',
        )
        read_only_fields = (
            'id',
        )


# Сериалайзер для Создание Песен 
class SoungCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soung
        fields = (
            'id',
            'title',
            'artist',
            'image',
            'genres',
            'file',
        )
        read_only_fields = (
            'id',
        )


# Сериалайзер для Альбома
class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    soungs = SoungSerializer(many=True)
    class Meta:
        model = Album
        fields = (
            'id',
            'title',
            'description',
            'artist',
            'soungs',
        )
        read_only_fields = (
            'id',
        )


# Сериалайзер для Создание Альбома 
class AlbumCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = (
            'id',
            'title',
            'description',
            'artist',
            'soungs',
        )
        read_only_fields = (
            'id',
        )


# Сериалайзер для Плейлиста
class PlaylistSerializer(serializers.ModelSerializer):
    soungs = SoungSerializer(many=True)
    class Meta:
        model = Playlist
        fields = (
            'id',
            'title',
            'user',
            'soungs',
        )
        read_only_fields = (
            'id',
            'user',
        )


# Сериалайзер для Создание Плейлиста 
class PlaylistCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = (
            'id',
            'title',
            'user',
            'soungs',
        )
        read_only_fields = (
            'id',
            'user',
        )
