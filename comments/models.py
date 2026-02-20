from django.db import models

from fans.models import Fan
from matches.models import Match


class Comment(models.Model):

    fan = models.ForeignKey(
        Fan, on_delete=models.CASCADE,
        related_name='fan_comments'
    )
    match = models.ForeignKey(
        Match, on_delete=models.CASCADE,
        related_name='match_comments'
    )
    text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,

    )

    def __str__(self):
        return f'{self.fan.name} on {self.match}: {self.text}'
