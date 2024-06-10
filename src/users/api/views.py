from django.shortcuts import render
from rest_framework.response import Response
from users.models import UserPaginator
from users.api.serializers import UserSerializer
from rest_framework.generics import ListAPIView
from users.repositories.repository import UserRepository



class UserListView(ListAPIView):
    queryset = UserRepository.get_all()
    
    serializer_class = UserSerializer
    pagination_class = UserPaginator