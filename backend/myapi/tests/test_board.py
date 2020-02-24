import json

from rest_framework.test import APITestCase

from myapi.tests.user_token import UserToken


class BoardTest(APITestCase, UserToken):
    title = 'test_title'
    content = 'test_content'

    def test_board_creating(self):
        user = self.create_user_mock()
        auth = self.get_jwt_token()

        result = self.client.post('/board/', json.dumps({
            'title': self.title,
            'content': self.content
        }), content_type='application/json', HTTP_AUTHORIZATION=auth)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data['title'], self.title)
        self.assertEqual(result.data['content'], self.content)
        self.assertEqual(result.data['author'], user.id)

    def test_board_creating_twice(self):
        pass

    def test_board_creating_without_title(self):
        pass

    def test_board_creating_without_content(self):
        pass

    def test_board_creating_without_author(self):
        pass

    def test_board_creating_without_jwt(self):
        result = self.client.post('/board/', json.dumps({
            'title': self.title,
            'content': self.content
        }), content_type='application/json')

        self.assertEqual(result.status_code, 401)
