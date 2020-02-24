import json

from django.test import Client

from myapi.tests.user_mock import UserMock


class UserToken(UserMock):

    def get_jwt_token(self):
        token = self.client.post('/api/token/', json.dumps({
            'username': self.username,
            'password': self.password
        }), content_type='application/json').json()['token']

        return 'jwt {0}'.format(token)
