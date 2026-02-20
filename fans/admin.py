from django.contrib import admin

from comments.models import Comment
from fans.models import Fan


@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ('name','location','favourite_player')
