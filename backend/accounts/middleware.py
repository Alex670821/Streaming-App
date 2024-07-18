# backend/accounts/middleware.py
import time
from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from accounts.models import UserPoints
from django.contrib.auth import get_user_model

User = get_user_model()

class UserPointsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            try:
                user_points = UserPoints.objects.get(user=request.user)
                now = timezone.now()
                if user_points.last_login_time:
                    delta = now - user_points.last_login_time
                    minutes = delta.total_seconds() // 60
                    if minutes >= 1:
                        user_points.add_points(int(minutes))
                user_points.last_login_time = now
                user_points.save()
            except UserPoints.DoesNotExist:
                UserPoints.objects.create(user=request.user, last_login_time=timezone.now())
