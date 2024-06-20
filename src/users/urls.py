from django.urls import path
from knox import views as knox_views

from users.api.views import (
    LoginView,
    SelfCreateView,
    SelfListView,
    SelfUpdateDeleteView,
    SelfView,
)

urlpatterns = [
    path('users/', SelfListView.as_view(), name='users-list'),
    path('user_change/<int:id>', SelfUpdateDeleteView.as_view(), name='user-change'),
    path('user_create/', SelfCreateView.as_view(), name='user-create'),
    path('user/<int:id>', SelfView.as_view(), name='user-view'),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),

]
