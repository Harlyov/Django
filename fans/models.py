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

    def __str__(self):
        return f'{self.name} - {self.location}'