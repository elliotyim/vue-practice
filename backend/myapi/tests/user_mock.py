from model_mommy import mommy

from myapi.models import User


class UserMock:
    username = 'test123'
    email = 'test123@test.com'
    password = '1111'

    def create_user_mock(self, user):
        return User.objects.create_user(
            username=user.username,
            email=user.email,
            password=user.password
        )
