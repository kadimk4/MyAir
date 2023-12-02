from django.urls import path
from planes.api.views import *

urlpatterns = [
    path('test/', PlaneView.as_view({'get': 'list'})),
    path('test/<str:code>/', PlaneView.as_view({'get': 'retrieve'})),
]
