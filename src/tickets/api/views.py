from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from core.factories.rep_factory import RepositoryFactory
from tickets.api.serializers import TicketRequestSerializer
from tickets.models import BaseTicketPagination
from tickets.schemas import SelfCreateViewSchema, SelfUpdateViewSchema, SelfViewSchema


@extend_schema(tags=['Tickets'])
class SelfListView(GenericAPIView):

    def get(self, request: Request) -> Response[list[dict[str, str]]]:
        repository = RepositoryFactory.create('ticket')
        queryset = repository.get_all()
        return Response(data=queryset, status=status.HTTP_200_OK)

    serializer_class: ModelSerializer = TicketRequestSerializer
    pagination_class: PageNumberPagination = BaseTicketPagination


@extend_schema(tags=['Tickets'])
class SelfView(GenericAPIView):
    serializer_class: ModelSerializer = TicketRequestSerializer

    @extend_schema(
        parameters=SelfViewSchema()
    )
    def get(self, request: Request, ticket_id: int) -> Response[list[dict[str, str]]]:
        repository = RepositoryFactory.create('ticket')
        serializer = repository.get(ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)


@extend_schema(tags=['Tickets'])
class SelfCreateView(GenericAPIView):
    serializer_class: ModelSerializer = TicketRequestSerializer

    @extend_schema(
        request=SelfCreateViewSchema()
    )
    def post(self, request: Request) -> Response[list[dict[str, str]]]:
        repository = RepositoryFactory.create('ticket')
        serializer = repository.post(request=request)
        if serializer:
            return Response(data=serializer, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Tickets'])
class SelfUpdateDeleteView(GenericAPIView):
    serializer_class: ModelSerializer = TicketRequestSerializer

    @extend_schema(
        parameters=SelfViewSchema(),
        request=SelfUpdateViewSchema()
    )
    def patch(self, request: Request, ticket_id: int) -> Response[list[dict[str, str]]]:
        repository = RepositoryFactory.create('ticket')
        serializer = repository.update(request=request, ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)

    @extend_schema(
        parameters=SelfViewSchema()
    )
    def delete(self, request: Request, ticket_id: int) -> Response[list[dict[str, str]]]:
        repository = RepositoryFactory.create('ticket')
        serializer = repository.delete(ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)
