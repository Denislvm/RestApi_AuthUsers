from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase, RequestsClient
from rest_framework import status
from rest_auth.authapp.models import username

class Test(APITestCase):
    def test_user(self):
        response = self.client.get('/users/4/')
        self.assertEqual(response.data, {'id': 4, 'username': 'fdgfdg'})


class UserTests(APITestCase):
    def test_create_users(self):
        url = reverse('user-list')
        data = {'username': 'vbcb'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(username.objects.count(), 1)
        self.assertEqual(username.objects.get().name, 'vbcb')
