import json

from rest_framework.test import APITestCase

from myapi.models import User


class MemberTest(APITestCase):
    username = 'test123'
    email = 'test123@test.com'
    password = '1111'

    def mock_user(self):
        User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )

    def test_signup(self):
        """
        Test a signing up request.
        """

        response = self.client.post('/signup/', json.dumps({
            'username': self.username,
            'email': self.email,
            'password': self.password
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def test_signup_twice(self):
        """
        Test signing up requests with the same information that causes the 400 error.
        """

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

    def test_signin(self):
        """
        Test signing in with jwt token.
        """

        self.mock_user()

        token = self.client.post('/api/token/', json.dumps({
            'username': self.username,
            'password': self.password
        }), content_type='application/json').json()['token']

        auth = 'jwt {0}'.format(token)
        response = self.client.post('/signin/', json.dumps({
            'username': self.username,
            'password': self.password
        }), content_type='application/json', HTTP_AUTHORIZATION=auth)

        self.assertEqual(response.status_code, 200)

    def test_signin_without_jwt(self):
        """
        Test signing in without jwt token that causes the authorization error.
        """

        self.mock_user()

        response = self.client.post('/signin/', json.dumps({
            'username': self.username,
            'password': self.password
        }), content_type='application/json')

        self.assertEqual(response.status_code, 401)
