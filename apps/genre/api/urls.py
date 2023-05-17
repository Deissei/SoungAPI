from rest_framework.routers import DefaultRouter

from apps.genre.api.views import GenreAPIViewSet


router = DefaultRouter()

router.register('genres', GenreAPIViewSet)

urlpatterns = router.urls
