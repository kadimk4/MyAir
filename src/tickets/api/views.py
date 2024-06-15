from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from tickets.api.serializers import TicketRequestSerializer, TicketResponseSerializer
from tickets.models import BaseTicketPagination
from drf_spectacular.views import extend_schema

from core.factories.rep_factory import RepositoryFactory
from tickets.schemas import SelfCreateViewSchema, SelfUpdateViewSchema, SelfViewSchema


@extend_schema(tags=['Tickets'])
class SelfListView(ListAPIView):
    repository = RepositoryFactory.create('ticket')
    queryset = repository.get_all()

    serializer_class = TicketRequestSerializer
    pagination_class = BaseTicketPagination

@extend_schema(tags=['Tickets'])
class SelfView(GenericAPIView):
    serializer_class = TicketRequestSerializer
    @extend_schema(
        parameters=SelfViewSchema()
    )
    
    
    def get(self,request, ticket_id):
        repository = RepositoryFactory.create('ticket')
        serializer = repository.get(ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)

@extend_schema(tags=['Tickets'])
class SelfCreateView(GenericAPIView):
    serializer_class = TicketRequestSerializer
    
    @extend_schema(
        request=SelfCreateViewSchema()
    )
    
    def post(self, request):
        repository = RepositoryFactory.create('ticket')
        serializer = repository.post(request=request)
        if serializer:
            return Response(data=serializer, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@extend_schema(tags=['Tickets'])
class SelfUpdateDeleteView(GenericAPIView):
    serializer_class = TicketRequestSerializer
    
    @extend_schema(
        parameters=SelfViewSchema(),
        request=SelfUpdateViewSchema()
    )
    def patch(self, request, ticket_id):
        repository = RepositoryFactory.create('ticket')
        serializer = repository.update(request=request, ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)

    @extend_schema(
        parameters=SelfViewSchema()
    )
    def delete(self, request, ticket_id):
        repository = RepositoryFactory.create('ticket')
        serializer = repository.delete(ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)
