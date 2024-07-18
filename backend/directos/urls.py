# backend/directos/urls.py
from django.urls import path
from .views import search_directos, UpdateRatingView

urlpatterns = [
    path('search/', search_directos, name='search_directos'),
    path('update-rating/', UpdateRatingView.as_view(), name='update_rating'),
]
