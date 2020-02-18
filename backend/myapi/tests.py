from django.test import TestCase, Client


class MemberTestCase(TestCase):
    username = 'test3'
    email = 'test@test.com'
    password = 'password'

    def test_signup(self):
        client = Client()
        response = client.post('/signup/', {
            'username': self.username,
            'email': self.email,
            'password': self.password
        }, 'application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json().get('detail'),
            'Welcome! you have signed up successfully.'
        )

    def test_signup_twice(self):
        client = Client()
        response = client.post('/signup/', {
            'username': self.username,
            'email': self.email,
            'password': self.password
        }, 'application/json')

        response = client.post('/signup/', {
            'username': self.username,
            'email': self.email,
            'password': self.password
        }, 'application/json')

        self.assertEqual(response.status_code, 400)
