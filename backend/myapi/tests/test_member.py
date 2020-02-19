import pytest
from django.test import Client


username = 'test11'
email = 'test11@test.com'
password = '111'


@pytest.mark.django_db
def test_signup():
    client = Client()
    response = client.post('/signup/', {
        'username': username,
        'email': email,
        'password': password
    }, 'application/json')

    assert response.status_code == 200


@pytest.mark.django_db
def test_signup_twice():
    client = Client()
    response = client.post('/signup/', {
        'username': username,
        'email': email,
        'password': password
    }, 'application/json')

    response = client.post('/signup/', {
        'username': username,
        'email': email,
        'password': password
    }, 'application/json')

    assert response.status_code == 400


@pytest.mark.django_db
def test_login():
    client = Client()
    response = client.post('/signin/', {

    }, 'application/json')

