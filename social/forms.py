from django import forms

from django.forms import ModelForm
from .models import Profile, Post, Comment



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["bio"]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = ['image', 'image_name', 'post_caption']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['comment']
