from django.db import models

# Create your models here.
from user_profile.models import User


class Tweet(models.Model):
    """
    Tweet model
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=160)
    created_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
