from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            "id",
            "title",
            "description",
            "category",
            "video_file",
            "is_active",
            "user",
            "uploaded_at",
            "scheduled_time",
        ]
        read_only_fields = ["user"]  # user debe ser de solo lectura
