from rest_framework.generics import get_object_or_404
from users.models import User


def is_valid_ticket(user_id):
    user = get_object_or_404(User, id=user_id)
    if user:
        return True
