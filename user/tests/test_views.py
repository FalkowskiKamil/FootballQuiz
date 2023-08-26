from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth


class TestViewsUser(TestCase):
    def setUp(self):
        self.client = Client()
        self.data = "test_1234"
        self.registration_url = reverse("user:register_request")
        self.login_url = reverse("user:login_request")
        self.logout_url = reverse("user:logout_request")

    def test_registration_get(self):
        response = self.client.get(self.registration_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "user/register.html")

    def test_logout_get(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 200)

    def test_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "user/login.html")

    def test_registration_post(self):
        response = self.client.post(
            self.registration_url,
            {
                "username": self.data,
                "psw": self.data,
                "firstname": self.data,
                "lastname": self.data,
            },
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.last().username, self.data)
        user = auth.get_user(self.client)
        self.assertEquals(user.is_authenticated, True)

    def test_logout_post(self):
        response = self.client.post(
            self.registration_url,
            {
                "username": self.data,
                "firstname": self.data,
                "lastname": self.data,
                "psw": self.data,
            },
        )
        user = auth.get_user(self.client)
        self.assertEquals(user.is_authenticated, True)
        response = self.client.post(self.logout_url)
        user = auth.get_user(self.client)
        self.assertEquals(user.is_authenticated, False)

    def test_login_post(self):
        self.client.post(
            self.registration_url,
            {
                "username": self.data,
                "firstname": self.data,
                "lastname": self.data,
                "psw": self.data,
            },
        )
        self.client.post(self.logout_url)
        response = self.client.post(
            self.login_url, {"username": self.data, "psw": self.data}
        )
        self.assertEquals(response.status_code, 200)
        user = auth.get_user(self.client)
        self.assertEquals(user.is_authenticated, True)

