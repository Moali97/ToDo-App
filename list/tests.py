from django.test import TestCase
from .models import List


class TestNewLists(TestCase):

    def setUp(self):
        List.objects.create(title='Go shopping for food')

    def test_text_content(self):
        list = List.objects.get(id=1)
        expected_object_name = f'{list.title}'
        self.assertEqual(expected_object_name, 'Go shopping for food')

# self.post = List.objects.create(
# title='Make some spicy food',
# )
