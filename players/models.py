from django.db import models

from common.choices import PlayerPosition
from players.validators import validate_age, validate_shirt_number


class Player(models.Model):
    name = models.CharField(
        max_length=50,

    )

    position = models.CharField(
        choices=PlayerPosition.choices,

    )

    shirt_number = models.PositiveIntegerField(
        validators=[validate_shirt_number],

    )

    age = models.PositiveIntegerField(
        validators=[validate_age],
    )

    photo_url = models.URLField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.name}-{self.shirt_number}'
