from rest_framework.routers import DefaultRouter

from apps.users.api.views import UserAPIViewSet


router = DefaultRouter()
router.register('users', UserAPIViewSet)

urlpatterns = router.urls
