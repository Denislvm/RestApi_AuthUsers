from django.shortcuts import render
from rest_framework import generics
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ModelViewSet
from authapp.serializers import UserDetailSerializer, UserListSerializer
from authapp.models import AuthUsers
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer

class ListUserView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = AuthUsers.objects.all()

class DetailUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = AuthUsers.objects.all()

