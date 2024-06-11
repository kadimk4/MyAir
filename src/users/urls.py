from django.urls import path
from users.api.views import SelfView, SelfListView

urlpatterns = [
    path('users/', SelfListView.as_view()),
    path('user_change/', SelfView.as_view()),
    
]
