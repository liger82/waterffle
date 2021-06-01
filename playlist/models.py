from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields.related import ManyToManyField


class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    genre_name = models.TextField()

# Create your models here.
class Music(models.Model):
    track_id = models.IntegerField(primary_key=True)
    filename = models.CharField(max_length=300) # 음악파일명
    artist_name = models.CharField(max_length=100)
    album_name = models.CharField(max_length=200)
    song_name = models.TextField()
    release_date = models.DateField()
    bit_rate = models.FloatField()
    # 한 곡의 genre는 여러 개일 수 있음.
    genres = ManyToManyField(Genre)
    features = ArrayField(models.FloatField())


class Playlist(models.Model):
    user_id = models.CharField(max_length=10) # ex) uid0000001
    track_id = models.ForeignKey(Music, on_delete=models.CASCADE) 
    # register_date = models.DateTimeField(auto_now_add=True)
    num_listen = models.IntegerField() # 재생된 횟수
