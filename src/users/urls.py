from django.urls import path

from users.api.views import SelfCreateView, SelfListView, SelfUpdareDeleteView

urlpatterns = [
    path('users/', SelfListView.as_view()),
    path('user_change/', SelfUpdareDeleteView.as_view()),
    path('user_create/', SelfCreateView.as_view())

]
