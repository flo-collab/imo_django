from django.test import TestCase
from django.test import Client


class RouteTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_up_loads_properly(self):
        response = self.client.get('/up/')
        self.assertEqual(response.status_code, 200)

    def test_post_csv_loads_properly(self):
        response = self.client.get('/up/post_csv/')
        self.assertEqual(response.status_code, 200)
        
