from rest_framework import serializers 

from apps.artist.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
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
