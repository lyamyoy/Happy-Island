from asyncio.windows_events import NULL
from email.policy import default
from time import timezone
from django.utils import timezone
from django.db import models
from django.forms import IntegerField

# Create your models here.


class Room(models.Model):
  room_name = models.CharField(max_length=64)
  member = models.IntegerField(default=0)

  def __str__(self):
    return f"{self.id}: {self.room_name} / {self.member}"


class User(models.Model):
  user_name = models.CharField(max_length=64)

  def __str__(self):
    return f"{self.id}: {self.user_name}"


class User_Room(models.Model):
  room_name = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="chat")
  user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="participants")
  joined_time = models.DateTimeField(default=timezone.now)


class Post(models.Model):
  post_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kuchikomi")
  where = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room", blank=True, null=True)
  text = models.CharField(max_length=280)
  post_time = models.DateTimeField(default=timezone.now)