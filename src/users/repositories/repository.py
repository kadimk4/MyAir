from django.http import HttpResponse
from rest_framework import status
from src.users.repositories.interface import BaseUser
from src.users.models import User


class UserRepository(BaseUser):
    
    def get(id):
        try:
            current_user = User.objects.get(id=id)
            return current_user
        except User.DoesNotExist:
            return HttpResponse('User does not exist', status=status.HTTP_404_NOT_FOUND)
        except User.MultipleObjectsReturned:
            return HttpResponse('There are many users with this id', status=status.HTTP_300_MULTIPLE_CHOICES)

    def post():
        pass

    def update():
        pass

    def delete():
        pass