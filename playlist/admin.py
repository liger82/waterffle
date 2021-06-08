from django.contrib import admin
from playlist.models import Genre, Music, Playlist

# Register your models here.
admin.site.register(Genre)
admin.site.register(Music)
admin.site.register(Playlist)