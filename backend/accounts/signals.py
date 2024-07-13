# accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserAccount, UserPoints

@receiver(post_save, sender=UserAccount)
def create_user_points(sender, instance, created, **kwargs):
    if created:
        UserPoints.objects.create(user=instance)

@receiver(post_save, sender=UserAccount)
def save_user_points(sender, instance, **kwargs):
    instance.points.save()
