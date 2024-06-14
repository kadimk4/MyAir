from django.urls import path

from amadeus_api.api.views import SelfView

urlpatterns = [
    path('amadeus/', SelfView.as_view(), name='amadeus-view')

]
