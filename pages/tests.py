from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class PagesTest(TestCase):
    def test_home_page_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_home_page_view_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
    def test_if_title_eq_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home Page')