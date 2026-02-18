from django.contrib import admin

from matches.models import Match


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('opponent_team','date','referee','stadium')
