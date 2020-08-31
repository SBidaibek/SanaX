from django.test import TestCase, Client

from rest_framework import status

from parameterized import parameterized

from backend.models import User


class TestAuth(TestCase):

    USERNAME = 'test_user'
    EMAIL = 'test_user@mail.test'
    PASSWORD = 'test123'

    @parameterized.expand([
        (USERNAME, EMAIL, PASSWORD, status.HTTP_200_OK),
        ('', EMAIL, PASSWORD, status.HTTP_400_BAD_REQUEST),
        (USERNAME, '', PASSWORD, status.HTTP_200_OK),
        (USERNAME, EMAIL, '', status.HTTP_400_BAD_REQUEST),
    ])
    def test_register(self, username, email, password, expected_status_code):
        data = {
            'username': username,
            'email': email,
            'password': password,
        }

        c = Client()
        response = c.post('/api/register/', data,
                          content_type='application/json')

        self.assertEqual(response.status_code, expected_status_code)

        if response.status_code == status.HTTP_200_OK:
            self.assertIn('user', response.data)
            self.assertIn('token', response.data)
            self.assertIn('id', response.data['user'])

            user = User.objects.get(id=response.data['user']['id'])

            self.assertEqual(user.email, email)
            self.assertEqual(user.username, username)

    @parameterized.expand([
        (USERNAME, PASSWORD, status.HTTP_200_OK),
        ('someone_not_registered', PASSWORD, status.HTTP_400_BAD_REQUEST),
        (USERNAME, 'wrong_password', status.HTTP_400_BAD_REQUEST),
    ])
    def test_login(self, username, password, expected_status_code):
        User.objects.create_user(self.USERNAME, self.EMAIL, self.PASSWORD)

        data = {
            'username': username,
            'password': password,
        }

        c = Client()
        response = c.post('/api/login/', data, content_type='application/json')

        self.assertEqual(response.status_code, expected_status_code)

        if response.status_code == status.HTTP_200_OK:
            self.assertIn('user', response.data)
            self.assertIn('token', response.data)
