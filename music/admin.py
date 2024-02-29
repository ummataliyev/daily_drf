from django.contrib import admin

from music import models

admin.site.register(models.Artist)
admin.site.register(models.Album)
admin.site.register(models.Song)
