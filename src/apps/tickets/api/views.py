from drf_spectacular.utils import extend_schema
from rest_framework import mixins, permissions, status
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from apps.tickets.api.serializers import TicketGetSerializer, TicketSerializer
from apps.tickets.schemas import SelfAMADEUSViewSchema, SelfViewSchema, SelfViewSchemaID
from utils.factories.rep_factory import RepositoryFactory
from utils.pagination import BasePagination


@extend_schema(tags=['Tickets'])
class SelfListView(mixins.ListModelMixin, GenericAPIView):
    pagination_class: PageNumberPagination = BasePagination
    permission_classes: list[BasePermission] = [permissions.IsAdminUser]
    authentication_classes: list[BaseAuthentication] = [SessionAuthentication]
    serializer_class: ModelSerializer = TicketGetSerializer

    def get_queryset(self) -> list[dict[str, str]]:
        repository = RepositoryFactory.create('ticket')
        return repository.get_all()

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)


@extend_schema(tags=['Tickets'])
class SelfUserTicketsView(GenericAPIView):
    pagination_class: PageNumberPagination = BasePagination
    permission_classes: list[BaseAuthentication] = [permissions.IsAuthenticated]
    authentication_classes: list[BaseAuthentication] = [SessionAuthentication]
    serializer_class: ModelSerializer = TicketGetSerializer

    def get(self, request) -> list[dict[str, str]]:
        repository = RepositoryFactory.create('ticket')
        response = repository.get_self_tickets(request)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Tickets'])
class SelfView(GenericAPIView):
    permission_classes: list[BasePermission] = [permissions.IsAuthenticated]
    authentication_classes: list[BaseAuthentication] = [SessionAuthentication]
    serializer_class: ModelSerializer = TicketGetSerializer

    @extend_schema(
        parameters=SelfViewSchemaID(),
        responses=TicketSerializer
    )
    def get(self, request: Request, ticket_id: int) -> Response[list[dict[str, str]]]:
        repository = RepositoryFactory.create('ticket')
        serializer = repository.get(ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)


@extend_schema(tags=['Tickets'])
class SelfCreateView(GenericAPIView):
    permission_classes: list[BasePermission] = [permissions.IsAuthenticated]
    authentication_classes: list[BaseAuthentication] = [SessionAuthentication]
    serializer_class: ModelSerializer = TicketGetSerializer

    @extend_schema(
        request=SelfAMADEUSViewSchema(),
        responses=TicketSerializer
    )
    def post(self, request: Request) -> dict[str, str]:
        repository = RepositoryFactory.create('ticket')
        serializer = repository.post(request)
        if serializer:
            return Response(data=serializer, status=status.HTTP_201_CREATED)
        return Response(data=serializer, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Tickets'])
class SelfUpdateDeleteView(GenericAPIView):
    permission_classes: list[BasePermission] = [permissions.IsAuthenticated]
    authentication_classes: list[BaseAuthentication] = [SessionAuthentication]
    serializer_class: ModelSerializer = TicketGetSerializer

    @extend_schema(
        parameters=SelfViewSchemaID(),
        request=SelfViewSchema(),
        responses=TicketSerializer
    )
    def patch(self, request: Request, ticket_id: int) -> Response[list[dict[str, str]]]:
        repository = RepositoryFactory.create('ticket')
        serializer = repository.update(request=request, ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)

    @extend_schema(
        parameters=SelfViewSchemaID(),
        responses=TicketSerializer
    )
    def delete(self, request: Request, ticket_id: int) -> Response[list[dict[str, str]]]:
        repository = RepositoryFactory.create('ticket')
        serializer = repository.delete(ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)
