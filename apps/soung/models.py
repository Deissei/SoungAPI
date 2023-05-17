from django.contrib.auth import get_user_model
from django.db import models

from apps.artist.models import Artist
from apps.genre.models import Genre

User = get_user_model()

class Soung(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='soung/image/', null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True, related_name='genre_soung')
    artist = models.ForeignKey(Artist, on_delete=models.SET_DEFAULT, default='None', related_name='soungs')
    file = models.FileField(upload_to='soung')

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist_album')
    soungs = models.ManyToManyField(Soung, related_name='soungs_album')

    def __str__(self):
        return self.title


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_playlist")
    title = models.CharField(max_length=256)
    soungs = models.ManyToManyField(Soung, related_name='soungs_playlist', blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('user', 'title')
        ordering = ('id', )