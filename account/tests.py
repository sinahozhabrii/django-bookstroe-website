from django.urls import reverse

from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
class SignUpTest(TestCase):
    username = 'testuser1'
    email = 'testuser1@gmail.com'
    def test_signup_view(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
    def test_signup_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
    def test_sign_up(self):

        user = get_user_model().objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
