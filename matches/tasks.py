from celery import shared_task
from .models import Match

@shared_task
def capitalize_opponent_match_teams(match_id):
    try:
        match = Match.objects.get(id=match_id)
        match.opponent_team = match.opponent_team.upper()
        match.save()
        print(f"Match {match_id} opponent team: {match.opponent_team}")
    except Match.DoesNotExist:
        print(f"Match {match_id} not found!")