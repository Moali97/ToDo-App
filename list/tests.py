from django.test import TestCase
from list.models import List


# Create your tests here.

class ListTestCase(TestCase):

    def setUp(self):
        List.objects.create(text='just a test')

    def test_text_content(self):
        list = List.objects.get(id=1)
        expected_object_name = f'{list.text}'
        self.assertEqual(expected_object_name, 'just a test')

