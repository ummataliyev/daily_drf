from django.db import models

from music.models.album import Album


class Song(models.Model):
    class Meta:
        db_table = 'song'

    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150, blank=False, null=False)
    picture = models.URLField(blank=True)
    source = models.URLField(blank=False, null=False)

    def __str__(self):
        return self.title
