# flake8: noqa: I001, I005

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('infra_app.urls', namespace='infra_app')),
    path('admin/', admin.site.urls),
]
