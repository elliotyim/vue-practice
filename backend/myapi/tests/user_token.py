import json

from django.test import Client

from myapi.tests.user_mock import UserMock


class UserToken(UserMock):

    def get_jwt_token(self, user):
        token = self.client.post('/api/token/', json.dumps({
            'username': user.username,
            'password': user.password
        }), content_type='application/json').json()['token']

        return 'jwt {0}'.format(token)
