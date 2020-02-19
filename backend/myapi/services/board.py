import json

from rest_framework.decorators import api_view

from myapi.models import Board


# @api_view(['POST'])
# def create_board(request):
#     request_body = json.loads(request.body.decode('utf-8'))
#     Board.objects.create(
#         title=request_body['title'],
#         content=request_body['content'],
#         author=author
#     )
#     return 200