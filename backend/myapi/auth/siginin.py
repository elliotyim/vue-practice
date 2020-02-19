from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView

from myapi.models import User
from myapi.serializers import UserSerializer


class Signin(APIView):

    def post(self, request, *args, **kwargs):
        # data = request.data
        # user = authenticate(username=data['username'], password=data['password'])
        #
        # if user is not None:
        #     login(request, user)
        #     return Response({'detail': 'Signed in successfully'})
        # else:
        #     return Response({'detail': 'Failed signing in'}, status=400)
        return Response()
