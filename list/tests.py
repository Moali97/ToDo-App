from django.test import TestCase
from .models import List
from django.test import SimpleTestCase


# tests for medels
class TestNewLists(TestCase):

    def setUp(self):
        List.objects.create(title='Go shopping for food')
        List.objects.create(date_created='2021-05-29')

    def test_text_content(self):
        list = List.objects.get(id=1)
        expected_object_name = f'{list.title}'
        self.assertEqual(expected_object_name, 'Go shopping for food')

    def test_date_content(self):
        list = List.objects.get(id=1)
        expected_object_name = f'{list.date_created}'
        self.assertEqual(expected_object_name, '2021-05-29')
