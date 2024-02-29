from django.db import models

from music.models.artist import Artist


class Album(models.Model):
    class Meta:
        db_table = 'album'

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=False, null=False)
    cover = models.URLField(blank=True)

    def __str__(self):
        return self.name
