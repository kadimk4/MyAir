from dataclasses import dataclass

from django.http import HttpResponse
from rest_framework import status
from users.repositories.interface import BaseUser
from users.models import User
from users.api.serializers import UserCreateSerializer


class UserRepository(BaseUser):
            
    def get(id):
        try:
            current_user = User.objects.get(id=id)
            return current_user
        except User.DoesNotExist:
            return HttpResponse('User does not exist', status=status.HTTP_404_NOT_FOUND)
        except User.MultipleObjectsReturned:
            return HttpResponse('There are many users with this id', status=status.HTTP_300_MULTIPLE_CHOICES)
    
    def get_all():
        users = User.objects.all()
        return users

    def post(request):
        serializer = UserCreateSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return serializer

    def update():
        pass

    def delete():
        pass