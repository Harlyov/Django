from django import forms

from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text','fan','match']

        widgets = {
            'text':forms.Textarea(attrs={
                'placeholder': 'Enter your comment here',

            })
        }

        error_messages = {
            'text':{
                'required': 'Please enter a comment.'
            }
        }
