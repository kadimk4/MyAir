from django.urls import path
from users.api.views import UserListView

urlpatterns = [
    path('users/', UserListView.as_view()),
]
