from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from myapi.models import User


class Signup(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Managing signing up of a new member
        """
        result = {"result": "회원가입 성공!"}
        request_body = json.loads(request.body.decode('utf-8'))

        username = request_body.get('username')
        email = request_body.get('email')
        password = request_body.get('password')

        User.objects.create_user(username=username, email=email, password=password)
        return Response(result)
