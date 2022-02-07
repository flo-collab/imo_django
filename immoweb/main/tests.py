from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.contrib import auth

class RouteTestCase(TestCase):
    def setUp(self):
        self.response = self.client.get('http://127.0.0.1:8000')
        test_user = User.objects.create_user(username='toto', password='turlututu')
        test_user.save()

    def test_index_loads_properly(self):
        self.assertEqual(self.response.status_code, 200)

    def test_login(self):
        self.client.login(username='toto', password='turlututu')
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_not_logged(self):
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_logout(self):
        self.client.login(username='toto', password='turlututu')
        self.client.logout()
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)
    
