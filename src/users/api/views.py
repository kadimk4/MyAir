from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes, OpenApiExample
from core.factories.rep_factory import RepositoryFactory
from users.api.serializers import UserRequestSerializer, UserResponseSerializer
from users.models import BaseUserPagination

@extend_schema(tags=['Users'])
class SelfListView(ListAPIView):

    repository = RepositoryFactory.create('user')
    queryset = repository.get_all()

    serializer_class = UserResponseSerializer
    pagination_class = BaseUserPagination

@extend_schema(tags=['Users'])
class SelfView(GenericAPIView):
    serializer_class = UserRequestSerializer
    
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                examples=[
                    OpenApiExample(
                        name='User ID',
                        value=1261
                    )
                ],
                required=True
            )
        ]
    )
    def get(self, request, id):
        repository = RepositoryFactory.create('user')
        serializer = repository.get(id)
        return Response(data=serializer, status=status.HTTP_200_OK)
@extend_schema(tags=['Users'])
class SelfCreateView(GenericAPIView):
    serializer_class = UserRequestSerializer
    
    @extend_schema(
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'first_name': {'type': 'string', 'example': 'Johnny'},
                    'last_name': {'type': 'string', 'example': 'Sins'},
                    'username': {'type': 'string', 'example': 'johnnysins1978'},
                    'email': {'type': 'string', 'example': 'johnnysinsavia@example.ru'},
                    'link': {'type': 'string', 'example': 'johnny_hub'},
                    'password': {'type': 'string', 'example': 'johnnycool'},
                    'passport': {
                        'type': 'string',
                        'format': 'binary',
                        'example': 'image.jpg'
                    }
                }
            }
        }
    )
    def post(self, request):
        repository = RepositoryFactory.create('user')
        serializer = repository.post(request)
        if serializer:
            return Response(data=serializer, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@extend_schema(tags=['Users'])
class SelfUpdateDeleteView(GenericAPIView):
    serializer_class = UserRequestSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH)
        ],
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'first_name': {'type': 'string', 'example': 'Johnny'},
                    'last_name': {'type': 'string', 'example': 'Sins'},
                    'username': {'type': 'string', 'example': 'johnnysins1978'},
                    'email': {'type': 'string', 'example': 'johnnysinsavia@example.ru'},
                    'link': {'type': 'string', 'example': 'johnny_hub'},
                    'password': {'type': 'string', 'example': 'johnnycool'},
                    'passport': {
                        'type': 'string',
                        'format': 'binary',
                        'example': 'image.jpg'
                    }
                }
            }
        }
    )
    def patch(self, request, id):
        repository = RepositoryFactory.create('user')
        serializer = repository.update(request, id)
        return Response(serializer, status=status.HTTP_200_OK)
    
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                examples=[
                    OpenApiExample(
                        name='User ID',
                        value=5123
                    )
                ],
                required=True
            )
        ],
    )
    def delete(self, request, id):
        repository = RepositoryFactory.create('user')
        serializer = repository.delete(id)
        return Response(serializer, status=status.HTTP_200_OK)
