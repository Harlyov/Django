from django.db import models

from players.models import Player


class Match(models.Model):
    date = models.DateField(

    )

    opponent_team = models.CharField(
        max_length=50,

    )

    players = models.ManyToManyField(
        Player,
        related_name='matches',
    )

    score_goal_real_madrid = models.PositiveIntegerField(

    )

    score_goal_opponent = models.PositiveIntegerField(

    )

    referee = models.CharField(
        max_length=100,
    )

    stadium = models.CharField(
        max_length=50,

    )

    def __str__(self):
        return f"Real Madrid vs {self.opponent_team} on {self.date}"