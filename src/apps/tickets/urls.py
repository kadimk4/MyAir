from django.urls import path

from apps.tickets.api.views import (
    SelfCreateView,
    SelfListView,
    SelfTicketsView,
    SelfUpdateDeleteView,
    SelfView,
)

urlpatterns = [
    path('ticket_list/', SelfListView.as_view(), name='ticket_list'),
    path('ticket_update/<int:ticket_id>', SelfUpdateDeleteView.as_view(), name='ticket_update'),
    path('ticket_create/', SelfCreateView.as_view(), name='ticket_post'),
    path('ticket/<int:ticket_id>', SelfView.as_view(), name='ticket_get'),
    path('ticket_self/', SelfTicketsView.as_view(), name='ticket_self'),
]
