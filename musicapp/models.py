from django.db import models
from django.utils.timezone import datetime



class Artiste(models.Model):
    first_name = models.CharField(default="", max_length=255, blank=False, null=False)
    last_name = models.CharField(default="", max_length=255, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False, default="")


    class Meta:
        ordering = ("first_name", "last_name", "age")

    
    def __str__(self):  
        return self.first_name


class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE, default="", blank=False, null=False)
    title = models.CharField(max_length=255, default="", blank=False, null=False)
    date_released = models.DateField(default=datetime.now, blank=False, null=False)
    likes = models.IntegerField(default=0, blank=False, null=False)
    id_artiste = models.CharField(max_length=100, default="", blank=False, null=False, unique=True, editable=True, primary_key=True)


    class Meta:
        ordering = ("title", "artiste", "date_released", "likes", "id_artiste",)


    def __str__(self):
        return self.title


class Lyric(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, default="", blank=False, null=False)
    content = models.TextField(default="", blank=False, null=False)
    id_song = models.CharField(max_length=100, default="", blank=False, null=False, unique=True, editable=True, primary_key=True)


    class Meta:
        ordering = ("song", "content", "id_song",)


    def __str__(self):
        return self.content

