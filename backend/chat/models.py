# chat/models.py
from django.db import models
from django.conf import settings
from directos.models import Directo

class ChatMessage(models.Model):
    directo = models.ForeignKey(Directo, on_delete=models.CASCADE, related_name='chat_messages')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}: {self.message}"
