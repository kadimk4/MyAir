from django.urls import path

from tickets.api.views import SelfListView, SelfUpdateDeleteView, SelfCreateView, SelfView

urlpatterns = [
    path('tickets/', SelfListView.as_view()),
    path('ticket_change/', SelfUpdateDeleteView.as_view()),
    path('ticket_create/', SelfCreateView.as_view()),
    path('ticket/<int:id>', SelfView.as_view()),

]
