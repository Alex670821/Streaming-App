# subscriptions/models.py

from django.db import models
from django.conf import settings


class Subscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    credit_card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)  # MM/YY format
    security_code = models.CharField(max_length=3)
    cedula = models.CharField(max_length=10)
    numero_celular = models.CharField(max_length=10)
    titular = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    referencia = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.email} Subscription"
