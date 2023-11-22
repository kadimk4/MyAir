from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from planes.api.views import *

urlpatterns = [
    path('test/', PlaneView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)