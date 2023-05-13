from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from apps.genre.serializers import GenreSerializer
from apps.genre.models import Genre


class GenreAPIViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUser]
