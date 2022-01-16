from django.test import TestCase, Client
from django.urls import reverse


class UrlsTestCase(TestCase):
    def setUp(self):
        client = Client()

    def test_can_access_base_url(self):
        response = self.client.get('/')

    def test_can_access_sitemap(self):
        response = self.client.get(reverse('sitemap'))
        self.assertEqual(response.status_code, 200)

    def test_can_access_robots(self):
        response = self.client.get(reverse('robots'))
        self.assertEqual(response.status_code, 200)

    def test_can_access_privacy(self):
        response = self.client.get(reverse('privacy'))
        self.assertEqual(response.status_code, 200)

    def test_can_access_contact(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_can_access_support(self):
        response = self.client.get(reverse('support'))
        self.assertEqual(response.status_code, 200)

    def test_can_access_info(self):
        response = self.client.get(reverse('info'))
        self.assertEqual(response.status_code, 200)
