import json

from rest_framework.test import APITestCase

from myapi.tests.user_token import UserToken


class MemberTest(APITestCase, UserToken):

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

    def test_signup_without_username(self):
        response = self.client.post('/signup/', json.dumps({
            'email': self.email,
            'password': self.password
        }), content_type='application/json')

        self.assertEqual(response.status_code, 400)

        # 에러 메시지 출력
        self.assertEqual(response.data['detail'], 400)

    def test_signup_without_password(self):
        response = self.client.post('/signup/', json.dumps({
            'username': self.username,
            'email': self.email
        }), content_type='application/json')

        self.assertEqual(response.status_code, 400)

        # 에러 메시지 출력
        # self.assertEqual(response.data['detail'], 400)

    def test_signup_without_email(self):
        response = self.client.post('/signup/', json.dumps({
            'username': self.username,
            'password': self.password
        }), content_type='application/json')

        self.assertEqual(response.status_code, 400)

        # 에러 메시지 출력
        # self.assertEqual(response.data['detail'], 400)

    def test_signin(self):
        """
        Test signing in with jwt token.
        """

        self.create_user_mock()
        auth = self.get_jwt_token()

        response = self.client.post('/signin/', json.dumps({
            'username': self.username,
            'password': self.password
        }), content_type='application/json', HTTP_AUTHORIZATION=auth)

        self.assertEqual(response.status_code, 200)

    def test_signin_without_jwt(self):
        """
        Test signing in without jwt token that causes the authorization error.
        """

        self.create_user_mock()

        response = self.client.post('/signin/', json.dumps({
            'username': self.username,
            'password': self.password
        }), content_type='application/json')

        self.assertEqual(response.status_code, 401)
