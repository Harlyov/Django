from django.contrib import admin

from players.models import Player


@admin.register(Player)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ('name','position','shirt_number','photo_url')

