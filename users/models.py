from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=10, default="")
    name = models.CharField(max_length=5, default="")
    gender = models.BooleanField(default = True)
    location = models.CharField(max_length=20, default="")
    disabled = models.CharField(max_length=10, default="")
    profileImage = models.ImageField(upload_to='profile/', default='default.png')
    introduction = models.CharField(max_length=150, default="")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
