from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

api_urlpattrens = [
    path('a1/', include('apps.artist.urls')),
    path('a2/', include('apps.soung.urls')),
]

urlpatterns += api_urlpattrens

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)