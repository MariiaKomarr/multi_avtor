from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'autofocus': True
            }
        )
        
        self.fields['email'].widget = forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email address'
            }
        )
        
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
        
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            }
        )
        
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
