from django.urls import path

from users.api.views import SelfCreateView, SelfListView, SelfUpdateDeleteView, SelfView

urlpatterns = [
    path('users/', SelfListView.as_view(), name='users-list'),
    path('user_change/<int:id>', SelfUpdateDeleteView.as_view(), name='user-change'),
    path('user_create/', SelfCreateView.as_view(), name='user-create'),
    path('user/<int:id>', SelfView.as_view(), name='user-view')

]
