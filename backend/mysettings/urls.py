from django.contrib import admin
from django.urls import path, include
from django.conf.urls import (
    handler400, handler404, handler403, handler500
)
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

handler404 = 'myapi.views.page_not_found_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', obtain_jwt_token),
    path('api/token/verify', verify_jwt_token),
    path('api/token/refresh', refresh_jwt_token),
    path('', include('myapi.myrouter')),
]
