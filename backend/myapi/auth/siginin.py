from rest_framework.response import Response
from rest_framework.views import APIView


class Signin(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        return Response({"test": "yap!"})
