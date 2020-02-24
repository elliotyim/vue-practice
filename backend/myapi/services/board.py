import base64
import json

import jwt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from myapi.models import User, Board
from myapi.serializers import BoardSerializer
from mysettings.settings import SECRET_KEY


@api_view(['POST'])
def create_board(request):
    auth = request.headers['Authorization']
    user_id = jwt.decode(auth[4:], SECRET_KEY, algorithms='HS256').get('user_id')
    user = User.objects.get(pk=user_id)

    request_body = json.loads(request.body.decode('utf-8'))

    board = Board.objects.create(title=request_body['title'], content=request_body['content'], author=user)

    return Response(BoardSerializer(board).data)
