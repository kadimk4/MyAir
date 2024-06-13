from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from core.factories.rep_factory import RepositoryFactory
from users.api.serializers import UserCrudSerializer, UserSerializer
from users.models import UserPaginator


class SelfListView(ListAPIView):

    repository = RepositoryFactory.create('user')
    queryset = repository.get_all()

    serializer_class = UserSerializer
    pagination_class = UserPaginator


class SelfView(GenericAPIView):
    serializer_class = UserSerializer

    def get(self, request, id):
        repository = RepositoryFactory.create('user')
        serializer = repository.get(request, id)
        return Response(data=serializer, status=status.HTTP_200_OK)


class SelfCreateView(GenericAPIView):
    serializer_class = UserCrudSerializer

    def post(self, request):
        repository = RepositoryFactory.create('user')
        serializer = repository.post(request)
        if serializer:
            return Response(data=serializer, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SelfUpdateDeleteView(GenericAPIView):
    serializer_class = UserCrudSerializer

    def patch(self, request, id):
        repository = RepositoryFactory.create('user')
        serializer = repository.update(request=request, user_id=id)
        return Response(serializer, status=status.HTTP_200_OK)

    def delete(self, request, id):
        repository = RepositoryFactory.create('user')
        serializer = repository.delete(user_id=id)
        return Response(serializer, status=status.HTTP_200_OK)
