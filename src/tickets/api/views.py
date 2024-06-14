from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes, OpenApiExample
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from tickets.api.serializers import TicketRequestSerializer, TicketResponseSerializer
from tickets.models import TicketPagination
from drf_spectacular.views import extend_schema

from core.factories.rep_factory import RepositoryFactory


@extend_schema(tags=['Tickets'])
class SelfListView(ListAPIView):
    repository = RepositoryFactory.create('ticket')
    queryset = repository.get_all()

    serializer_class = TicketRequestSerializer
    pagination_class = TicketPagination

@extend_schema(tags=['Tickets'])
class SelfView(GenericAPIView):
    serializer_class = TicketRequestSerializer
    
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="ticket_id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                examples=[
                    OpenApiExample(
                        name='Ticket ID example',
                        summary='Example of a ticket ID',
                        description='Example showing how to specify a ticket ID',
                        value=1251
                    )
                ],
                required=True
            )
        ],
        responses=TicketResponseSerializer,
        request=TicketRequestSerializer,
        description='Getting a ticket'
    )
    
    def get(self,request, ticket_id):
        repository = RepositoryFactory.create('ticket')
        serializer = repository.get(ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)

@extend_schema(tags=['Tickets'])
class SelfCreateView(GenericAPIView):
    serializer_class = TicketRequestSerializer
    
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="code",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Code',
                        value='JET321USA262RUS',
                        summary='Example code 1',
                        description='Code example for post'
                    ),
                    OpenApiExample(
                        name='Example 2 - Code',
                        value='ECO518RUS951USA',
                        summary='Example code 2',
                        description='Code example for post'
                    )
                ],
                required=True
            ),
            OpenApiParameter(
                name="place_code",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Place Code',
                        value='12J',
                        summary='Example place code 1',
                        description='Place code example for post'
                    ),
                    OpenApiExample(
                        name='Example 2 - Place Code',
                        value='4A',
                        summary='Example place code 2',
                        description='Place code example for post'
                    )
                ],
                required=True
            ),
            OpenApiParameter(
                name="user_id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - User ID',
                        value=5012,
                        summary='Example user ID 1',
                        description='User ID example for post'
                    ),
                    OpenApiExample(
                        name='Example 2 - User ID',
                        value=231,
                        summary='Example user ID 2',
                        description='User ID example for post'
                    )
                ],
                required=True
            ),
            OpenApiParameter(
                name="date",
                type=OpenApiTypes.DATE,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Date',
                        value='2021-10-10',
                        summary='Example date 1',
                        description='Date example for post'
                    ),
                    OpenApiExample(
                        name='Example 2 - Date',
                        value='2022-01-21',
                        summary='Example date 2',
                        description='Date example for post'
                    )
                ],
                required=True
            )
        ],
        responses=TicketResponseSerializer,
        request=TicketRequestSerializer,
        description='Post ticket'
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
        parameters=[
            OpenApiParameter("ticket_id", OpenApiTypes.INT, OpenApiParameter.PATH),
            OpenApiParameter(
                name="code",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Code',
                        value='JET321USA262RUS',
                        summary='Example code 1',
                        description='Code example for update'
                    ),
                    OpenApiExample(
                        name='Example 2 - Code',
                        value='ECO518RUS951USA',
                        summary='Example code 2',
                        description='Code example for update'
                    )
                ]
            ),
            OpenApiParameter(
                name="place_code",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Place Code',
                        value='12J',
                        summary='Example place code 1',
                        description='Place code example for update'
                    ),
                    OpenApiExample(
                        name='Example 2 - Place Code',
                        value='4A',
                        summary='Example place code 2',
                        description='Place code example for update'
                    )
                ]
            ),
            OpenApiParameter(
                name="user_id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - User ID',
                        value=5012,
                        summary='Example user ID 1',
                        description='User ID example for update'
                    ),
                    OpenApiExample(
                        name='Example 2 - User ID',
                        value=231,
                        summary='Example user ID 2',
                        description='User ID example for update'
                    )
                ]
            ),
            OpenApiParameter(
                name="date",
                type=OpenApiTypes.DATE,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Date',
                        value='2021-10-10',
                        summary='Example date 1',
                        description='Date example for update'
                    ),
                    OpenApiExample(
                        name='Example 2 - Date',
                        value='2022-01-21',
                        summary='Example date 2',
                        description='Date example for update'
                    )
                ]
            )
        ],
        responses=TicketResponseSerializer,
        request=TicketRequestSerializer,
        description='Update ticket'
    )
    def patch(self, request, ticket_id):
        repository = RepositoryFactory.create('ticket')
        serializer = repository.update(request=request, ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)

    @extend_schema(
        parameters=[
            OpenApiParameter("ticket_id", OpenApiTypes.INT, OpenApiParameter.PATH, examples=[
                OpenApiExample(
                    name='Ticket delete example 1',
                    summary='Example 1',
                    description='Delete Ticket',
                    value=1203
                ),
                OpenApiExample(
                    name='Ticket delete example 2',
                    summary='Example 2',
                    description='Delete Ticket',
                    value=510
                )
            ])
        ],
        description='Delete ticket'
    )
    def delete(self, request, ticket_id):
        repository = RepositoryFactory.create('ticket')
        serializer = repository.delete(ticket_id=ticket_id)
        return Response(data=serializer, status=status.HTTP_200_OK)
