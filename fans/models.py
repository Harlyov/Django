from django.db import models
from django.db.models import CASCADE

from matches.models import Match
from players.models import Player


class Fan(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,

    )

    location = models.CharField(
        max_length=100,

    )

    favourite_player =models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
    )


class Comment(models.Model):

    fan = models.ForeignKey(
        Fan, on_delete=models.CASCADE,
        related_name='comments'
    )
    match = models.ForeignKey(
        Match, on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,

    )

    def __str__(self):
        return f'{self.fan.name} on {self.match}: {self.text}'



