from django.test import TestCase
from .models import Profile, Post, Comment


class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james = Profile(
            first_name='Ian', last_name='Muriuki', email='james@moringaschool.com')
