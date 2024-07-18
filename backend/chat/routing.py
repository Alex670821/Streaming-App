# chat/routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<int:directo_id>/', consumers.ChatConsumer.as_asgi()),
]
