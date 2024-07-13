from rest_framework import serializers
from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

    def create(self, validated_data):
        validated_data["is_active"] = True  # Cambiar is_active a True
        return super().create(validated_data)
