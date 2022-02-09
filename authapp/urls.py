from django.contrib import admin
from django.urls import path, include
from authapp.views import *

urlpatterns = [
    path('POST/user/', CreateUserView.as_view(), name='post_user'),
    path('user-list/', ListUserView.as_view(), name='users'),
    path('user/<int:pk>/', DetailUserView.as_view(), name='user'),
]