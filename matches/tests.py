from django.test import TestCase
from django.urls import reverse
from model_bakery import baker
from matches.models import Match
from matches.forms import MatchForm, MatchDeleteForm
from players.models import Player
from datetime import date
from django.contrib.auth import get_user_model

class MatchesTests(TestCase):

    def setUp(self):
        self.player_1 = baker.make(Player)
        self.player_2 = baker.make(Player)

    def test_match_form_valid(self):
        form_data = {
            'date': date.today(),
            'opponent_team': 'Barcelona',
            'score_goal_real_madrid': 2,
            'score_goal_opponent': 1,
            'referee': 'John Doe',
            'stadium': 'Santiago Bernabeu',
            'players':[self.player_1.id,self.player_2.id]
        }
        form = MatchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_match_form_invalid_missing_fields(self):
        form_data = {
            'date': date.today(),
            'score_goal_real_madrid': 2,
        }
        form = MatchForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('opponent_team', form.errors)

    def test_match_create_with_players(self):
        match = baker.make(Match)
        match.players.add(self.player_1, self.player_2)
        self.assertEqual(match.players.count(), 2)

    def test_match_delete_form_readonly(self):
        match = baker.make(Match)
        form = MatchDeleteForm(instance=match)
        for field in form.fields.values():
            self.assertTrue(field.disabled)

    def test_match_update_valid(self):
        player = baker.make('players.Player')
        match = baker.make(Match, opponent_team='Old Team')
        match.players.add(player)

        form_data = {
            'date': match.date,
            'opponent_team': 'New Team',
            'score_goal_real_madrid': match.score_goal_real_madrid,
            'score_goal_opponent': match.score_goal_opponent,
            'referee': match.referee,
            'stadium': match.stadium,
            'players': [player.id],
        }

        form = MatchForm(data=form_data, instance=match)
        self.assertTrue(form.is_valid())  # вече ще мине
        updated_match = form.save()
        self.assertEqual(updated_match.opponent_team, 'New Team')
        self.assertIn(player, updated_match.players.all())

    def test_match_update_invalid(self):
        match = baker.make(Match)
        form_data = {
            'date': match.date,
            'opponent_team': '',
            'score_goal_real_madrid': -1,
        }
        form = MatchForm(data=form_data, instance=match)
        self.assertFalse(form.is_valid())
        self.assertIn('opponent_team', form.errors)
        self.assertIn('score_goal_real_madrid', form.errors)

    def test_match_str_method(self):
        match = baker.make(Match, opponent_team='Valencia', date=date(2026,4,2))
        self.assertEqual(str(match), f"Real Madrid vs Valencia on 2026-04-02")

    def test_match_list_view(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='pass1234')
        self.client.login(username='testuser', password='pass1234')

        match = baker.make(Match)
        response = self.client.get(reverse('matches:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, match.opponent_team)

    def test_match_form_fields_required(self):
        form = MatchForm(data={})

        self.assertFalse(form.is_valid())
        self.assertIn('opponent_team', form.errors)
        self.assertIn('score_goal_real_madrid', form.errors)
        self.assertIn('score_goal_opponent', form.errors)
        self.assertIn('referee', form.errors)
        self.assertIn('stadium', form.errors)