from rest_framework import serializers

from music import models
from music.serializers.artist import ArtistSerializer


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = models.Album
        fields = '__all__'
