# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatMessage
from directos.models import Directo
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.directo_id = self.scope['url_route']['kwargs']['directo_id']
        self.room_group_name = f'chat_{self.directo_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_email = text_data_json['user']
        
        try:
            user = await User.objects.get(email=user_email)
            directo = await Directo.objects.get(id=self.directo_id)
            chat_message = await ChatMessage.objects.create(user=user, directo=directo, message=message)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'user': user_email,
                }
            )
        except Exception as e:
            print(f"Error: {e}")

    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
        }))
