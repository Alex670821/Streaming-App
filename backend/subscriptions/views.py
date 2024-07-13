from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Subscription
from .serializers import SubscriptionSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_subscription(request):
    user = request.user
    data = request.data.copy()
    data["user"] = user.id
    data["is_active"] = True  # Cambiar is_active a True

    serializer = SubscriptionSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def check_subscription(request):
    user = request.user
    try:
        subscription = Subscription.objects.get(user=user)
        is_active = subscription.is_active
    except Subscription.DoesNotExist:
        is_active = False

    return Response({"is_active": is_active})
