from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.soung.views import (
    SoungAPIViewSet,
    AlbumAPIViewSet,
    PlaylistAPIViewSet
)

router = DefaultRouter()

router.register('songs', SoungAPIViewSet)
router.register('albums', AlbumAPIViewSet)
router.register('playlists', PlaylistAPIViewSet)

urlpatterns = router.urls