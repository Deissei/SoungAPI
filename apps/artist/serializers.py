from rest_framework import serializers 

from apps.artist.models import Artist


class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = (
            'name',
            'bio',
        )


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = (
            'id',
            'name',
            'bio',
            'date_of_birth',
        )
