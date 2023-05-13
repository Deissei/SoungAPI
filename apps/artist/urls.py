from rest_framework.routers import DefaultRouter

from apps.artist.views import ArtistAPIViewSet


router = DefaultRouter()

router.register('', ArtistAPIViewSet)


urlpatterns = router.urls
