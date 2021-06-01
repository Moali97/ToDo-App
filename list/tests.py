from django.test import TestCase
from .models import List
from django.urls import reverse


# tests models
class ModelListsTest(TestCase):

    def setUp(self):
        List.objects.create(title='Go shopping for food')
        List.objects.create(date_created='2021-05-29')

    def test_text_content(self):
        list = List.objects.get(id='1')
        expected_object_name = f'{list.title}'
        self.assertEqual(expected_object_name, 'Go shopping for food')

    def test_date_content(self):
        list = List.objects.get(id=1)
        expected_object_name = f'{list.date_created}'
        self.assertEqual(expected_object_name, '2021-06-01')


# testing views
class HomePageViewTest(TestCase):
    def setUp(self):
        List.objects.create(title='This is a test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

