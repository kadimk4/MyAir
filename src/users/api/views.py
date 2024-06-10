from django.shortcuts import render
from rest_framework.response import Response
from users.models import UserPaginator
from users.api.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView
from users.repositories.repository import UserRepository



class UserListView(ListAPIView):
    queryset = UserRepository.get_all()
    
    serializer_class = UserSerializer
    pagination_class = UserPaginator

class UserCollectionView(APIView):
    
    def post(self, request):
        serializer = UserRepository.post(request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)