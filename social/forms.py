from django import forms

from django.forms import ModelForm
from .models import Profile, Post, Comment


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_picture", 'name']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = ['comment']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image', 'image_name', 'post_caption']
