# from dataclasses import dataclass

from rest_framework.generics import get_object_or_404
from users.repositories.interface import BaseUser
from users.models import User
from users.api.serializers import UserCrudSerializer


class UserRepository(BaseUser):
   
    def get_all() -> list[dict]:
        users_list = User.objects.values(
            'id',
            'username',
            'first_name',
            'last_name',
            'link',
            'email',
        )
        return users_list

    def post(request) -> dict[str]:
        serializer = UserCrudSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.data
        
        serializer.save()
        
        return {'id': user['id'],
                'username': user['username'],
                'fist_name': user['first_name'],
                'last_name': user['last_name'],
                'link': user['link'],
                'email': user['email'],
        }

    def update(request) -> dict[str]:
        user_id = request.data.get('id')
        user = get_object_or_404(User, pk=user_id)
        serializer = UserCrudSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return {'id': user.id,
                'username': user.username,
                'fist_name': user.first_name,
                'last_name': user.last_name,
                'link': user.link,
                'email': user.email,
        }

    def delete(self, request) -> dict[str]:
        user_id = request.data.get('id')
        user = get_object_or_404(User, pk=user_id)
        user.delete()

        return {'id': user.id,
                'username': user.username,
                'fist_name': user.first_name,
                'last_name': user.last_name,
                'link': user.link,
                'email': user.email,
        }