from distutils.command import upload

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile (models.Model):
    '''
    profile class holding all the models
    '''
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_keys=True)
    name = TextField(default="Anonymous")
    profile_picture = models.ImageField(upload_to='users/' default='T')
    bio = models.TextField(default="Tell us more")

    def save_profile(self):
        self.save()


class Post(models.Model):

    '''
    user post of images and the comments
    '''
    image = models.Image(upload_to='posts/')
    user = models.ForeignKey(Profile, related_name='posts')
    post_caption = TextField(default=False)
    created = models.DateField(auto_now_add=True, db_index=True)

    def post(self):
        self.save()


class comment(model.Model):
    '''
    comments model for users
    '''
    comment = models.TextField()
    post = models.ForeignKey(post, related='comments')
    user =models.ForeignKey(Profile, related_name='comments')
    likes = models.BooleanField(default=False)

    def save_image(self):
        self.save()




