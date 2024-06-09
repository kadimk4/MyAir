from src.users.repositories.interface import BaseUser
from src.users.models import User


class UserRepository(BaseUser):
    
    def get(id):
        return User.objects.get(id=id)

    def post():
        pass

    def update():
        pass

    def delete():
        pass