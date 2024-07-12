# subscriptions/urls.py

from django.urls import path
from .views import create_subscription, check_subscription

urlpatterns = [
    path("create/", create_subscription, name="create_subscription"),
    path("status/", check_subscription, name="check_subscription"),
]
