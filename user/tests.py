from django.test import TestCase
from django.urls import reverse


class UserAuthTestCase(TestCase):
    def setUp(self):
        self.register_url = reverse("user:register")
        self.login_url = reverse("user:login_request")
        self.logout_url = reverse("user:logout_request")

    def test_register(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get(self.logout_url, follow=True)
        self.assertEqual(response.status_code, 200)
