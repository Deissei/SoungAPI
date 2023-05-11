from rest_framework.routers import DefaultRouter

from apps.soung.views import (
    SoungAPIViewSet,
    AlbumAPIViewSet,
)

router = DefaultRouter()

router.register('soungs', SoungAPIViewSet)
router.register('albums', AlbumAPIViewSet)

urlpatterns = router.urls
