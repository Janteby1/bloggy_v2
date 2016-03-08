from django import forms
from .models import UserProfile, Post
# these are already given to us 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, CheckboxInput


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("first_name", "last_name","username", "email", "password1", "password2")

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ("m_name",)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]
        widgets = {
            "content": Textarea(attrs={"cols": 60, "rows": 10})
        }
