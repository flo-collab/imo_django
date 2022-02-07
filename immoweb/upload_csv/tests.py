from django.test import TestCase
from django.test import Client

# Create your tests here.
def test_route_up():
    c = Client()
    response = c.get('/up/')
    assert response.status_code == 200

class RouteTestCase(TestCase):
    def test_up_loads_properly(self):
        # The index page loads properly
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)
    



# def test_index_loads_properly(self):
#     # The upload page loads properly
#     response = self.client.get('http://127.0.0.1:8000')
#     self.assertEqual(response.status_code, 200)