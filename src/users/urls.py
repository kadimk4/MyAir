from django.urls import path

from users.api.views import SelfCreateView, SelfListView, SelfUpdateDeleteView, SelfView

urlpatterns = [
    path('users/', SelfListView.as_view()),
    path('user_change/', SelfUpdateDeleteView.as_view()),
    path('user_create/', SelfCreateView.as_view()),
    path('user/<int:id>', SelfView.as_view())

]
