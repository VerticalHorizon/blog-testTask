from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import signup

urlpatterns = [
    path('signup/', signup, name='create-user'),
    path('signin/', obtain_jwt_token, name='create-token'),
    path('refresh/', refresh_jwt_token, name='refresh-token'),
    path('verify/', verify_jwt_token, name='verify-token'),
]