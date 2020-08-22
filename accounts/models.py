from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(default="default.jpg", upload_to="profile_pics", blank=True)
    #email = models.EmailField(unique=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# class User1(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     reg_at = models.DateTimeField(default=timezone.now)
#     photo = models.ImageField(default="default.jpg", upload_to="profile_pics")
#
#
#     def __str__(self):
#         return 'Profile for user {}'.format(self.user.username)
