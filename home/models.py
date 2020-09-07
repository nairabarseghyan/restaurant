from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Food(models.Model):
    food_name = models.CharField(max_length=100, blank=True, null=True)
    food_photo = models.ImageField(default="profile_pics/log.jpg", upload_to="foods", blank=True)


    def __str__(self):
        return self.food_name
