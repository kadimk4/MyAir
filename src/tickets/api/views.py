# from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from tickets.api.serializers import TicketSerializer
from tickets.models import TicketPagination


from core.factories.rep_factory import RepositoryFactory


# Create your views here.
class SelfListView(ListAPIView):
    repository = RepositoryFactory.create('ticket')
    queryset = repository.get_all()

    serializer_class = TicketSerializer
    pagination_class = TicketPagination


class SelfView(GenericAPIView):
    serializer_class = TicketSerializer

    def get(self,request, ticket_id):
        repository = RepositoryFactory.create('ticket')
        serializer = repository.get(ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)


class SelfCreateView(GenericAPIView):
    serializer_class = TicketSerializer

    def post(self, request):
        repository = RepositoryFactory.create('ticket')
        serializer = repository.post(request=request)
        if serializer:
            return Response(data=serializer, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SelfUpdateDeleteView(GenericAPIView):
    serializer_class = TicketSerializer

    def patch(self, request, ticket_id):
        repository = RepositoryFactory.create('ticket')
        serializer = repository.update(request=request, ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)

    def delete(self, request, ticket_id):
        repository = RepositoryFactory.create('ticket')
        serializer = repository.delete(ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)
