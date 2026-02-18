from django.contrib import admin

from fans.models import Fan,Comment


@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ('name','location','favourite_player')



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('fan','match','text','created_at')