from django.contrib import admin
from .models import Artiste, Song, Lyric



admin.site.site_header = "Music App"
admin.site.site_title = "Music App Admin Portal"


class ArtisteAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age")
    
admin.site.register(Artiste, ArtisteAdmin)


class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "artiste", "date_released", "likes", "id_artiste")

admin.site.register(Song, SongAdmin)


class LyricAdmin(admin.ModelAdmin):
    list_display = ("song", "id_song")

admin.site.register(Lyric, LyricAdmin)
