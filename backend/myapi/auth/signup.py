from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ParseError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from myapi.models import User


class Signup(APIView):
    permission_classes = [AllowAny]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        """
        Managing signing up of a new member
        """

        result = {"detail": "Welcome! you have signed up successfully."}
        request_body = json.loads(request.body.decode('utf-8'))

        username = request_body.get('username')
        email = request_body.get('email')
        password = request_body.get('password')

        try:
            User.objects.create_user(username=username, email=email, password=password)
        except Exception as e:
            raise ParseError(detail=e)

        return Response(result)
