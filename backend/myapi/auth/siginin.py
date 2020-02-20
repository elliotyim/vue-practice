import json

from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView

from myapi.models import User
from myapi.serializers import UserSerializer


class Signin(APIView):

    def post(self, request, *args, **kwargs):
        request_body = json.loads(request.body.decode('utf-8'))
        queryset = User.objects.get(username=request_body['username'])
        return Response(UserSerializer(queryset).data)
