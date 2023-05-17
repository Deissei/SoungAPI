from rest_framework import serializers 

from apps.artist.models import Artist
from apps.soung.models import Soung

from apps.genre.api.serializers import GenreSerializer

class SoungsSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Soung
        fields = (
            'id',
            'title',
            'image',
            'genres',
            'file',
        )
        read_only_fields = (
            'id',
        )


class ArtistSerializer(serializers.ModelSerializer):
    soungs = SoungsSerializer(many=True)
    class Meta:
        model = Artist
        fields = (
            'id',
            'name',
            'image',
            'soungs',
            'bio',
            'date_of_birth',
        )
        read_only_fields = (
            "id",
        )


class ArtistCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = (
            'id',
            'name',
            'image',
            'bio',
            'date_of_birth',
        )
        read_only_fields = (
            "id",
        )
