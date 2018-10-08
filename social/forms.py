from django.forms import ModelForm
from .models import Profile, Post, Comment



class ProfileInfo(ModelForm):
    class meta:
        model = 