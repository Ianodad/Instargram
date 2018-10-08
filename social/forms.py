from django import forms

from django.forms import ModelForm
from .models import Profile, Post, Comment



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["username"]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        exclude = ['post', 'user', 'date_posted', 'Likes']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['user', 'created']
