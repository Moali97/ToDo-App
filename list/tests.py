from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import List


class TestNewLists(TestCase):

    def setUp(self):
        pass

        self.post = List.objects.create(
            title='Make some spicy food',

        )

def test_post_content(self):
    self.assertEqual(f'{self.post.title}', 'A good title')