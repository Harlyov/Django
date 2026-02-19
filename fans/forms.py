from django import forms
from fans.models import Fan

class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter fan name'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter fan location'}),
        }
        error_messages = {
            'name': {
                'required': 'Fan name is required.',
                'max_length': 'Name cannot be longer than 50 characters.',
            },
            'location': {
                'required': 'Location is required.',
                'max_length': 'Location cannot be longer than 100 characters.',
            },
            'favourite_player': {
                'required': 'Please select a favourite player.',
            },
        }
