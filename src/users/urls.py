from django.urls import path

from users.api.views import SelfListView, SelfView

urlpatterns = [
    path('users/', SelfListView.as_view()),
    path('user_change/', SelfView.as_view()),

]
