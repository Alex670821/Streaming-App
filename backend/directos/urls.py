# directos/urls.py
from django.urls import path
from .views import search_directos

urlpatterns = [
    path('search/', search_directos, name='search_directos'),
]
