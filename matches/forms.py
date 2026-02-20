from django import forms

from matches.models import Match


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = "__all__"

        widgets = {
            'opponent_team': forms.TextInput(attrs={'placeholder': 'Enter opponent team name'}),
            'referee': forms.TextInput(attrs={'placeholder': 'Enter referee name'}),
            'stadium': forms.TextInput(attrs={'placeholder': 'Enter stadium name'}),
        }

        error_messages = {
            'opponent_team': {
                'required': 'Please enter opponent team name.',
                'max_length': 'Team name is too long.',
            },
            'score_goal_real_madrid': {
                'required': 'Enter Real Madrid score.',
                'invalid': 'Must be a positive number.',
            },
            'score_goal_opponent': {
                'required': 'Enter opponent score.',
                'invalid': 'Must be a positive number.',
            },
        }



class MatchDeleteForm(MatchForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


        for field in self.fields.values():
            field.disabled = True