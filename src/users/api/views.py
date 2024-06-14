from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes, OpenApiExample
from core.factories.rep_factory import RepositoryFactory
from users.api.serializers import UserRequestSerializer, UserResponseSerializer
from users.models import UserPaginator

@extend_schema(tags=['Users'])
class SelfListView(ListAPIView):

    repository = RepositoryFactory.create('user')
    queryset = repository.get_all()

    serializer_class = UserResponseSerializer
    pagination_class = UserPaginator

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
                        name='User ID example',
                        summary='Example of a user ID',
                        description='Example showing how to specify a user ID',
                        value=5123
                    )
                ],
                required=True
            )
        ],
        responses=UserResponseSerializer,
        request=UserRequestSerializer,
        description='Getting a user'
    )
    def get(self, request, id):
        repository = RepositoryFactory.create('user')
        serializer = repository.get(id)
        return Response(data=serializer, status=status.HTTP_200_OK)
@extend_schema(tags=['Users'])
class SelfCreateView(GenericAPIView):
    serializer_class = UserRequestSerializer
    
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="first_name",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - First name',
                        value='Johnny ',
                        summary='Example first name 1',
                        description='First name example for post'
                    ),
                    OpenApiExample(
                        name='Example 2 - First name',
                        value='Yriy',
                        summary='Example first name 2',
                        description='First name example for post'
                    )
                ],
                required=True
            ),
            OpenApiParameter(
                name="last_name",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Last name',
                        value='Sins',
                        summary='Example last name 1',
                        description='Last name example for post'
                    ),
                    OpenApiExample(
                        name='Example 2 - Last name',
                        value='Shevchyk',
                        summary='Example last name 2',
                        description='Last name example for post'
                    )
                ],
                required=True
            ),
            OpenApiParameter(
                name="username",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Username',
                        value='johnnycool1978',
                        summary='Example username 1',
                        description='Username example for post'
                    ),
                    OpenApiExample(
                        name='Example 2 - Username',
                        value='qq2yra',
                        summary='Example username 2',
                        description='Username example for post'
                    )
                ],
                required=True
            ),
            OpenApiParameter(
                name="email",
                type=OpenApiTypes.EMAIL,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Email',
                        value='johnnysins@example.ru',
                        summary='Example email 1',
                        description='Email example for post'
                    ),
                    OpenApiExample(
                        name='Example 2 - Email',
                        value='qq2006@example.ru',
                        summary='Example email 2',
                        description='Email example for post'
                    )
                ],
                required=True
            ),
            OpenApiParameter(
                name="link",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Link',
                        value='user_domain/<link>',
                        summary='Example link 1',
                        description='Link example for post'
                    )
                ],
                required=True
            ),
            OpenApiParameter(
                name="password",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Password',
                        value='johnnysins1978secret',
                        summary='Example password 1',
                        description='Password example for post'
                    ),
                    OpenApiExample(
                        name='Example 2 - Password',
                        value='qq2006itquestions',
                        summary='Example password 2',
                        description='Password example for post'
                    )
                ],
                required=True
            ),
            OpenApiParameter(
                name="passport",
                type=OpenApiTypes.BINARY,
                location="media",
                required=True
            )
        ],
        responses=UserResponseSerializer,
        request=UserRequestSerializer,
        description='Post user'
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
                location=OpenApiParameter.PATH,
                examples=[
                    OpenApiExample(
                        name='Example 1 - User ID',
                        value=8912,
                        summary='Example user ID 1',
                        description='user ID example for update'
                    ),
                    OpenApiExample(
                        name='Example 2 - User ID',
                        value=791,
                        summary='Example user ID 2',
                        description='user ID example for update'
                    )
                ]
                ),
            OpenApiParameter(
                name="first_name",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - First name',
                        value='Johnny ',
                        summary='Example first name 1',
                        description='First name example for update'
                    ),
                    OpenApiExample(
                        name='Example 2 - First name',
                        value='Yriy',
                        summary='Example first name 2',
                        description='First name example for update'
                    )
                ],
            ),
            OpenApiParameter(
                name="last_name",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Last name',
                        value='Sins',
                        summary='Example last name 1',
                        description='Last name example for update'
                    ),
                    OpenApiExample(
                        name='Example 2 - Last name',
                        value='Shevchyk',
                        summary='Example last name 2',
                        description='Last name example for update'
                    )
                ],
            ),
            OpenApiParameter(
                name="username",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Username',
                        value='johnnycool1978',
                        summary='Example username 1',
                        description='Username example for update'
                    ),
                    OpenApiExample(
                        name='Example 2 - Username',
                        value='qq2yra',
                        summary='Example username 2',
                        description='Username example for update'
                    )
                ],
            ),
            OpenApiParameter(
                name="email",
                type=OpenApiTypes.EMAIL,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Email',
                        value='johnnysins@example.ru',
                        summary='Example email 1',
                        description='Email example for update'
                    ),
                    OpenApiExample(
                        name='Example 2 - Email',
                        value='qq2006@example.ru',
                        summary='Example email 2',
                        description='Email example for update'
                    )
                ],
            ),
            OpenApiParameter(
                name="link",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Link',
                        value='user_domain/<link>',
                        summary='Example link 1',
                        description='Link example for update'
                    )
                ],
            ),
            OpenApiParameter(
                name="password",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        name='Example 1 - Password',
                        value='johnnysins1978secret',
                        summary='Example password 1',
                        description='Password example for update'
                    ),
                    OpenApiExample(
                        name='Example 2 - Password',
                        value='qq2006itquestions',
                        summary='Example password 2',
                        description='Password example for update'
                    )
                ],
            ),
            OpenApiParameter(
                name="passport",
                type=OpenApiTypes.BINARY,
                location="media",
            )
        ],
        responses=UserResponseSerializer,
        request=UserRequestSerializer,
        description='Update user'
    )
    
    def patch(self, request, id):
        repository = RepositoryFactory.create('user')
        serializer = repository.update(request, id)
        return Response(serializer, status=status.HTTP_200_OK)
    
    @extend_schema(
        parameters=[
            OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH, examples=[
                OpenApiExample(
                    name='User delete example 1',
                    summary='Example 1',
                    description='Delete User',
                    value=1251
                ),
                OpenApiExample(
                    name='User delete example 2',
                    summary='Example 2',
                    description='Delete User',
                    value=5521
                )
            ])
        ],
        description='Delete user'
    )
    
    def delete(self, request, id):
        repository = RepositoryFactory.create('user')
        serializer = repository.delete(id)
        return Response(serializer, status=status.HTTP_200_OK)
