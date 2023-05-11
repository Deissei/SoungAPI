from django.contrib.auth import get_user_model
from django.db import models

from apps.artist.models import Artist


User = get_user_model()

class Soung(models.Model):
    title = models.CharField(max_length=256, unique=True)
    artist = models.ForeignKey(Artist, on_delete=models.SET_DEFAULT, default='None')
    file = models.FileField(upload_to='soung')

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist_album')
    soungs = models.ManyToManyField(Soung, related_name='soungs_album')

    def __str__(self):
        return self.title


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, unique=True)
    soungs = models.ManyToManyField(Soung, related_name='soungs_playlist')
    
    def __str__(self):
        return self.title
