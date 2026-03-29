from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age', 'bio', 'password1', 'password2']


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'Please enter your username'})
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Please enter your password here.'})
    )