# chat/urls.py
from django.urls import path
from .views import get_chat_messages, send_chat_message

urlpatterns = [
    path('messages/<int:directo_id>/', get_chat_messages, name='get_chat_messages'),
    path('messages/send/', send_chat_message, name='send_chat_message'),
]
