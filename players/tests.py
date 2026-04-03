from django.test import TestCase
from model_bakery import baker
from players.models import Player

class PlayersModelTests(TestCase):
    def test_player_creation(self):
        player = baker.make(Player)
        self.assertIsNotNone(player.id)
        self.assertTrue(player.name)