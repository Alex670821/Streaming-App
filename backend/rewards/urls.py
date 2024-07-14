# rewards/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RewardViewSet

router = DefaultRouter()
router.register(r'rewards', RewardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
