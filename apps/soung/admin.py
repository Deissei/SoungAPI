from django.contrib import admin

from apps.soung.models import (
    Soung,
    Album,
    Playlist
)


admin.site.register(Soung)
admin.site.register(Album)
admin.site.register(Playlist)