from rest_framework import serializers
from matches.models import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = [
            'id',
            'date',
            'opponent_team',
            'score_goal_real_madrid',
            'score_goal_opponent',
            'referee',
            'stadium',
        ]