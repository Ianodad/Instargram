from distutils.command import upload

from django.contrib.auth.models import User
from django.db import models
from pyuploadcare.dj.models import ImageField


# Create your models here.

class Profile(models.Model):
    '''
    profile class holding all the models
    '''
    username = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    name = models.TextField(default="Anonymous")
    profile_picture = ImageField(
        manual_crop='200x200')
    bio = models.TextField(default="Tell us more")

    def save_profile(self):
        self.save()

    def update_Profile(self, update):
        self.profile_bio = update
        self.save()


class Post(models.Model):

    '''
    user post of images and the comments
    '''
    image = ImageField(manual_crop='800x800')
    image_name = models.TextField(default=False)
    user = models.ForeignKey(User, null=True, related_name='posts')
    post_caption = models.TextField(max_length="300")
    created = models.DateField(auto_now_add=True, db_index=True)

    def post(self):
        self.save()

    @classmethod
    def get_post(cls, id):
        post = Post.objects.filter(user= id)
        return post

    @classmethod
    def get_all_posts(cls):
        posts = Post.objects.all()
        return posts

    
class Comment(models.Model):
    '''
    comments model for users
    '''
    comment = models.TextField(null=True)
    post = models.ForeignKey(Post, related_name='comments')
    user = models.ForeignKey(Profile, related_name='comments')
    date_posted = models.DateTimeField(auto_now=True)
    likes = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_posted']

    def save_image(self):
        self.save()

    @classmethod
    def get_comment(cls, id):
        comments = Comment.objects.filter(post=id)
        return comments
