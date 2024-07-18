from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from .models import Video
from .serializers import VideoSerializer
from rest_framework.permissions import IsAuthenticated


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        now = timezone.now()
        # Activar videos programados si la hora programada ya pasó
        videos_to_activate = Video.objects.filter(
            scheduled_time__lte=now, is_active=False
        )
        for video in videos_to_activate:
            video.is_active = True
            video.save()
        # Solo devolver videos activos
        return Video.objects.filter(is_active=True)
