from django import forms
from django.forms import Textarea
from blog.models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]
        widgets = {
            "content": Textarea(attrs={"cols": 50, "rows": 10}),
        }
        
    def save(self, user):
        m = super(PostForm, self).save(commit=False)
        m.user = user
        m.save()
        return m


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
