from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from music import models


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Song
        fields = ('id', 'title', 'album', 'picture', 'source')

    def validate_source(self, value):
        if not value.endswith('.mp3'):
            raise ValidationError(detail="mp3 file is required!")

        return value
