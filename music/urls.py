from django.urls import path

from music import views


urlpatterns = [
    path('songs/', views.SongAPIView.as_view(), name='song'),
]
