from django.db import models


class PlayerPosition(models.TextChoices):
    goalkeeper = 'GK', 'Goalkeeper'
    central_back = 'CB', 'CentralBack'
    right_back = "RB", "RightBack"
    left_back = "LB", "LeftBack"
    central_mid = "CM", "CentralMid"
    central_attack_mid = "CAM", 'CentralAttackMid'
    defensive_mid = "DMF", 'DefensiveMid'
    right_wing = "RW", "RightWing"
    left_wing = "LW", "LeftWing"
    striker = "ST", "Striker"