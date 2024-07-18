from django.db import models
from accounts.models import UserAccount  # Asegúrate de importar el modelo correcto


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    video_file = models.FileField(upload_to="videos/")
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return self.title
