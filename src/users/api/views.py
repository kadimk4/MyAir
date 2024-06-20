from django.contrib.auth import login
from drf_spectacular.utils import extend_schema
from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView
from rest_framework import mixins, permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from core.factories.rep_factory import RepositoryFactory
from core.pagination import BasePagination
from users.api.serializers import AuthSerializer, UserListSerializer, UserSerializer
from users.schemas import SelfCreateViewSchema, SelfUpdateViewSchema, SelfViewSchema


@extend_schema(tags=['Users'])
class SelfListView(mixins.ListModelMixin, GenericAPIView):
    pagination_class = BasePagination
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    serializer_class = UserListSerializer

    def get_queryset(self) -> list[dict[str, str]]:
        repository = RepositoryFactory.create('user')
        return repository.get_all()

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)


@extend_schema(tags=['Users'])
class SelfView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [TokenAuthentication, SessionAuthentication]
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
    serializer_class = UserSerializer
    # permission_classes = (permissions.AllowAny,)
    # authentication_classes = [TokenAuthentication]

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
    authentication_classes = [TokenAuthentication, SessionAuthentication]
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


class LoginView(KnoxLoginView):
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            return super().post(request, format=None)
        else:
            return Response('Error during login', status=status.HTTP_400_BAD_REQUEST)
