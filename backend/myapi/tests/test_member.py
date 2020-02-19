import json

from django.contrib.auth.hashers import make_password
from django.test import Client
from rest_framework.test import APITestCase, APIClient
from rest_framework_jwt import utils

# username = 'admin'
# email = 'test11@test.com'
# password = '1111'
#
# jwt_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTgyNzc2NDI5LCJlbWFpbCI6ImFkbWluQHRlc3QuY29tIiwib3JpZ19pYXQiOjE1ODIxNzE2Mjl9._Wm-yO3Buhs6QkuIgohFng0dufjn930pXlCnqfz25EI'
#
#
# @pytest.mark.django_db
# def test_signup():
#     client = Client()
#     response = client.post('/signup/', {
#         'username': username,
#         'email': email,
#         'password': password
#     }, 'application/json')
#
#     assert response.status_code == 200
#
#
# @pytest.mark.django_db
# def test_signup_twice():
#     client = Client()
#     response = client.post('/signup/', {
#         'username': username,
#         'email': email,
#         'password': password
#     }, 'application/json')
#
#     response = client.post('/signup/', {
#         'username': username,
#         'email': email,
#         'password': password
#     }, 'application/json')
#
#     assert response.status_code == 400
#
#
# @pytest.mark.django_db
# def test_login(client):
#     response = client.post('/signin/', json={
#         'username': username,
#         'password': password
#     }, HTTP_AUTHORIZATiON='jwt {}'.format(jwt_token))
#
#     assert response.status_code == 200
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
