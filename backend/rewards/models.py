# rewards/models.py
from django.db import models
from accounts.models import UserAccount

class Reward(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='rewards/')
    points_cost = models.IntegerField()

    def __str__(self):
        return self.name

class UserReward(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    date_redeemed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} - {self.reward.name}'
