from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from rest_framework.permissions import AllowAny

from core.terms_of_service import terms_of_service

schema_view = get_schema_view(
    openapi.Info(
        title="API Songs, Artist Documentation",
        default_version='v1.0',
        description="My API for songs and artists that was needed for the final project",
        terms_of_service='TERMS_OF_USE',
        contact=openapi.Contact(email="kiradoni05@gmail.com"),
        license=openapi.License(name="IT Academy"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

router = routers.DefaultRouter()


from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/TERMS_OF_USE/', terms_of_service),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-auth/', include('rest_framework.urls')),
    path('token/create', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

api_urlpattrens = [
    path('artists/', include('apps.artist.urls')),
    path('', include('apps.soung.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.genre.urls')),
]

urlpatterns += api_urlpattrens

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
