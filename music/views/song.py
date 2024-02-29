from rest_framework.views import APIView
from rest_framework.response import Response


from music import models
from music import serializers


class SongAPIView(APIView):
    def get(self, request):
        songs = models.Song.objects.all()
        serializer = serializers.SongSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        song = serializer.save()

        return Response(data=serializer.data)
