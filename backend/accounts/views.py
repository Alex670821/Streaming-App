from rest_framework import generics, permissions
from .models import UserAccount
from .serializers import UserCreateSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
