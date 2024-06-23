from drf_spectacular.utils import extend_schema
from rest_framework import mixins, permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from apps.users.api.serializers import UserListSerializer, UserSerializer
from apps.users.schemas import (
    SelfCreateViewSchema,
    SelfUpdateViewSchema,
    SelfViewSchema,
)
from utils.factories.rep_factory import RepositoryFactory
from utils.pagination import BasePagination


@extend_schema(tags=['Users'])
class SelfListView(mixins.ListModelMixin, GenericAPIView):
    pagination_class = BasePagination
    permission_classes = (permissions.IsAdminUser,)
    authentication_classes = [SessionAuthentication]
    serializer_class = UserListSerializer

    def get_queryset(self) -> list[dict[str, str]]:
        repository = RepositoryFactory.create('user')
        return repository.get_all()

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)


@extend_schema(tags=['Users'])
class SelfView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [SessionAuthentication]
    serializer_class = UserSerializer

    @extend_schema(

        parameters=SelfViewSchema()

    )
    def get(self, request: Request, id: int) -> Response[list[dict[str, str]]]:
        repository = RepositoryFactory.create('user')
        serializer = repository.get(id)
        return Response(data=serializer, status=status.HTTP_200_OK)


@extend_schema(tags=['Users'])
class SelfCreateView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [SessionAuthentication]
    serializer_class = UserSerializer

    @extend_schema(
        request=SelfCreateViewSchema()
    )
    def post(self, request: Request) -> Response[list[dict[str, str]]]:
        repository = RepositoryFactory.create('user')
        serializer = repository.post(request)
        if serializer:
            return Response(data=serializer, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Users'])
class SelfUpdateDeleteView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [SessionAuthentication]
    serializer_class = UserSerializer

    @extend_schema(
        parameters=SelfViewSchema(),
        request=SelfUpdateViewSchema()
    )
    def patch(self, request: Request, id: int) -> Response[list[dict[str, str]]]:
        repository = RepositoryFactory.create('user')
        serializer = repository.update(request, id)
        return Response(serializer, status=status.HTTP_200_OK)

    @extend_schema(
        parameters=SelfViewSchema()
    )
    def delete(self, request: Request, id: int) -> Response[list[dict[str, str]]]:
        repository = RepositoryFactory.create('user')
        serializer = repository.delete(id)
        return Response(serializer, status=status.HTTP_200_OK)
