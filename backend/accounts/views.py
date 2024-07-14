# accounts/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.utils import timezone  # Asegúrate de importar timezone
from .serializers import UserProfileSerializer, ChangePasswordSerializer, UserPointsSerializer
from .models import UserPoints

User = get_user_model()

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            if not check_password(serializer.data.get("old_password"), user.password):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"status": "password set"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserPointsView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            points_instance = user.points
            serializer = UserPointsSerializer(points_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'User not authenticated'}, status=status.HTTP_400_BAD_REQUEST)

class UpdateUserPointsView(APIView):
    def post(self, request):
        user = request.user
        points_instance = user.points
        new_points = request.data.get('points', points_instance.points)
        points_instance.points = new_points
        points_instance.last_login_time = timezone.now()
        points_instance.save()
        return Response({'status': 'success', 'points': points_instance.points}, status=status.HTTP_200_OK)

class LogoutAndSavePointsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        points_instance = user.points
        new_points = request.data.get('points', points_instance.points)
        points_instance.points = new_points
        points_instance.last_login_time = timezone.now()
        points_instance.save()
        return Response({'status': 'success', 'points': points_instance.points}, status=status.HTTP_200_OK)
