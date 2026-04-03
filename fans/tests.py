from django.test import TestCase
from model_bakery import baker
from fans.models import Fan
from players.models import Player

class FansModelTests(TestCase):
    def test_fan_creation_with_player(self):
        player = baker.make(Player)
        fan = baker.make(Fan, favourite_player=player)
        self.assertEqual(fan.favourite_player, player)