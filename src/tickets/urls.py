from django.urls import path

from tickets.api.views import SelfListView, SelfUpdateDeleteView, SelfCreateView, SelfView

urlpatterns = [
    path('tickets/', SelfListView.as_view(), name='ticket_list'),
    path('ticket_update/<int:ticket_id>', SelfUpdateDeleteView.as_view(), name='ticket_update'),
    path('ticket_create/', SelfCreateView.as_view(), name='ticket_post'),
    path('ticket/<int:ticket_id>', SelfView.as_view(), name='ticket_get'),

]
