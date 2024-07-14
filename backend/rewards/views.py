# rewards/views.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Reward, UserReward
from .serializers import RewardSerializer, UserRewardSerializer

class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def redeem(self, request, pk=None):
        reward = self.get_object()
        user_points = request.user.points

        if user_points.points >= reward.points_cost:
            user_points.points -= reward.points_cost
            user_points.save()
            UserReward.objects.create(user=request.user, reward=reward)
            return Response({'status': 'reward redeemed'})
        else:
            return Response({'status': 'not enough points'}, status=status.HTTP_400_BAD_REQUEST)
