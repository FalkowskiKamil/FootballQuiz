from django.test import TestCase
from django.urls import reverse, resolve
from user.views import register_request, login_request, logout_request

class TestUrlsUser(TestCase):
    def test_register_url_is_resolved(self):
        url = reverse("user:register_request")
        self.assertEquals(resolve(url).func, register_request)
        
    def test_login_url_is_resolved(self):
        url = reverse("user:login_request")
        self.assertEquals(resolve(url).func, login_request)

    def test_logout_url_is_resolved(self):
        url = reverse("user:logout_request")
        self.assertEquals(resolve(url).func, logout_request)