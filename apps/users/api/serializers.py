from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.soung.models import Playlist

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
        )
    
    def create(self, validated_data):
        password = validated_data['password']
        if not password:
            raise serializers.ValidationError("Not Password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Playlist.objects.create(user=user, title="Избранные")
        return user
