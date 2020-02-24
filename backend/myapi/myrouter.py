from django.urls import path

from myapi.auth import signup
from myapi.auth.siginin import Signin
from myapi.auth.signup import Signup
from myapi.services.board import create_board

urlpatterns = [
    path('signup/', Signup.as_view(), name='register'),
    path('signin/', Signin.as_view(), name='login'),
    path('board/', create_board)
]
