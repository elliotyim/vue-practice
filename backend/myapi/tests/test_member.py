
import json

from rest_framework.test import APITestCase

from myapi.models import User


class MemberTest(APITestCase):
    username = 'test123'
    email = 'test123@test.com'
    password = '1111'

    def test_signup(self):
        response = self.client.post('/signup/', json.dumps({
            'username': self.username,
            'email': self.email,
            'password': self.password
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def test_signup_twice(self):
        self.client.post('/signup/', json.dumps({
            'username': self.username,
            'email': self.email,
            'password': self.password
        }), content_type='application/json')

        response = self.client.post('/signup/', json.dumps({
            'username': self.username,
            'email': self.email,
            'password': self.password
        }), content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_login(self):
        User.objects.create_user(
            username='test', email='test@test.com', password='1111'
        )

        token = self.client.post('/api/token/', json.dumps({
            'username': 'test',
            'password': '1111'
        }), content_type='application/json').json()['token']

        auth = 'jwt {0}'.format(token)
        response = self.client.post('/signin/', json.dumps({
            'username': 'test',
            'password': '1111'
        }), content_type='application/json', HTTP_AUTHORIZATION=auth)

        self.assertEqual(response.status_code, 200)
