# from dataclasses import dataclass

from rest_framework.generics import get_object_or_404
from rest_framework.request import Request

from apps.users.api.serializers import UserSerializer
from apps.users.models import User
from apps.users.services.email import is_valid_email
from utils.interface import BaseRepository


class UserRepository(BaseRepository):

    def get_all(self) -> list[dict]:
        users_list = User.objects.values(
            'id',
            'username',
            'first_name',
            'last_name',
            'link',
            'email',
        ).order_by('id')
        return users_list

    def get(self, id: int) -> dict[str, str]:
        user = get_object_or_404(User, pk=id)
        serializer = UserSerializer(user)
        return {
            'username': serializer.data['username'],
            'first_name': serializer.data['first_name'],
            'last_name': serializer.data['last_name'],
            'link': serializer.data['link'],
            'email': serializer.data['email'],
        }

    def post(self, request: Request) -> dict[str, str] | None:
        if is_valid_email(request.data['email']):
            user = User(
                username=request.data['username'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                email=request.data['email'],
                link=request.data['link'],
                passport=request.data['passport']
            )

            user.set_password(request.data['password'])

            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            user.save()

            return {
                'username': request.data['username'],
                'first_name': request.data['first_name'],
                'last_name': request.data['last_name'],
                'link': request.data['link'],
                'email': request.data['email'],
            }
        return None

    def update(self, request: Request, user_id: int) -> dict[str, str]:
        user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return {'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'link': user.link,
                'email': user.email,
                }

    def delete(self, user_id: int) -> dict[str, str]:
        user = get_object_or_404(User, pk=user_id)
        user_serializer = UserSerializer(user).data
        user.delete()
        return {'id': user_serializer['id'],
                'username': user_serializer['username'],
                'first_name': user_serializer['first_name'],
                'last_name': user_serializer['last_name'],
                'link': user_serializer['link'],
                'email': user_serializer['email'],
                }
