# rewards/serializers.py
from rest_framework import serializers
from .models import Reward, UserReward

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ['id', 'name', 'description', 'image', 'points_cost']

class UserRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReward
        fields = ['user', 'reward', 'date_redeemed']
