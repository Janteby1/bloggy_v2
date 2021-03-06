from django import forms
from users.models import User
from django.forms import PasswordInput


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]
        widgets = {
            "password": PasswordInput()        
        }
