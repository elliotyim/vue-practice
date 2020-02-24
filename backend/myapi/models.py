from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('The given email must be set')
        elif not password:
            raise ValueError('The given password must be set')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **kwargs):
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_user(email, password, **kwargs)


class User(AbstractUser):
    photo_name = models.CharField(max_length=255, null=True)
    tel = models.CharField(max_length=15, null=True)
    is_verified = models.BooleanField(default=False)
    verification_key = models.CharField(max_length=255, null=True)

    objects = MyUserManager()


class Board(models.Model):
    title = models.CharField(max_length=30, null=False)
    content = models.TextField(null=False)
    author = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.title
