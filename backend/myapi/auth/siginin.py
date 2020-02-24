import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.views import APIView

from myapi.models import User
from myapi.serializers import UserSerializer


class Signin(APIView):

    def post(self, request, *args, **kwargs):
        request_body = json.loads(request.body.decode('utf-8'))

        user = User.objects.get(email=request_body['email'])
        if user.password == make_password(request_body['password']):
            Response('Successfully signed in!')
        else:
            raise Exception('Failed to signin!')
