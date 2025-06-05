from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/widgets/', include('widgets.urls')),
]
