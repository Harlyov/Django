from django import forms
from django.core.exceptions import ValidationError

from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'position', 'shirt_number', 'age', ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter player name'}),

        }
        error_messages = {
            'name': {
                'required': 'Player name is required.',
                'max_length': 'Name cannot be longer than 50 characters.',
            },
            'position': {
                'required': 'Please select a position for the player.',
            },
            'shirt_number': {
                'required': 'Shirt number is required.',
                'invalid': 'Enter a valid number between 1 and 99.',
            },
            'age': {
                'required': 'Age is required.',
                'invalid': 'Enter a valid age (16 or older).',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        shirt_number = cleaned_data.get('shirt_number')

        return cleaned_data
