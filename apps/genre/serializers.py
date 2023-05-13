from rest_framework import serializers

from apps.genre.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'id',
            'title',
            'url',
        )
        read_only_fields = (
            'id',
            'url',
        )