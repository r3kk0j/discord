from django.db import models
from django.contrib.auth.models import User

class Channel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    channel = models.ForeignKey(Channel, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content[:20]}'

class DatabaseTest(models.Model):
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)