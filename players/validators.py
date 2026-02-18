from django.core.exceptions import ValidationError


def validate_age(value):
    if value < 16:
        raise ValidationError("Age of the player must be at least 16.")


def validate_shirt_number(value):
    if value < 1 or value > 99:
        raise ValidationError("The shirt number must be between 1 and 99.")
