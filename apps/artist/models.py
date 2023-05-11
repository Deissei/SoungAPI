from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=256, unique=True)
    bio = models.TextField()
    image = models.ImageField(upload_to='artists/', null=True, blank=True)
    date_of_birth = models.DateTimeField()

    def __str__(self):
        return self.name
