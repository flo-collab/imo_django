from django.test import TestCase
from django.test import Client
from django.core import mail
import numpy as np
import django

class RouteTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get('/visualize/')

    def test_visualize_loads_properly(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_visualize_context_not_blank(self):
        self.assertFalse(self.response.context == None)

    def test_visualize_context_keys(self):
        self.assertTrue('biens' in self.response.context)
        self.assertTrue('villes' in self.response.context)
        self.assertTrue('mean_price' in self.response.context)
    
    def test_visualize_context_type_mean_price(self):
        self.assertTrue(type(self.response.context['mean_price'])==np.float64)
    
    def test_visualize_context_type_mean_price(self):
        self.assertTrue(type(self.response.context['biens'])==django.db.models.query.QuerySet)

    def test_visualize_context_type_mean_price(self):
        self.assertTrue(type(self.response.context['villes'])==django.db.models.query.QuerySet)


class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail('Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')