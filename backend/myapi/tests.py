from django.test import TestCase, Client


class MemberTestCase(TestCase):
    def test_sign_up(self):
        username = 'test3'
        email = 'test@test.com'
        password = 'password'

        client = Client()
        response = client.post('/signup/', {
            'username': username,
            'email': email,
            'password': password
        }, 'application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json().get('detail'),
            'Welcome! you have signed up successfully.'
        )

        response = client.post('/signup/', {
            'username': username,
            'email': email,
            'password': password
        }, 'application/json')

        self.assertEqual(response.status_code, 400)
