# backend/directos/models.py
from django.db import models

class Directo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    video_url = models.URLField(default='https://www.youtube.com/embed/dQw4w9WgXcQ')
    rating = models.IntegerField(default=0)  # Agregar el campo de calificación

    def __str__(self):
        return self.title
