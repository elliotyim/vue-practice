from rest_framework.response import Response
from rest_framework.views import APIView

from myapi.models import User
from myapi.serializers import UserSerializer


class Signin(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        queryset = User.objects.filter(username=data['username'])
        return Response(UserSerializer(queryset).data)
