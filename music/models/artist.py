from django.db import models


class Artist(models.Model):
    class Meta:
        db_table = 'artist'

    name = models.CharField(max_length=150, blank=True, null=False)
    picture = models.URLField(blank=True)

    def __str__(self):
        return self.name
