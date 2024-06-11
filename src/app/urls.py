from django.contrib import admin
from django.urls import include, path

from app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls'))
]


if settings.DEBUG:
    urlpatterns = [
        *urlpatterns,
        path('__debug__/', include('debug_toolbar.urls')),
    ]
