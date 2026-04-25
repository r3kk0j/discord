from django.db import models

class DatabaseTest(models.Model):
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Channel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    # Naprawione: było on_on_delete, ma być on_delete
    channel = models.ForeignKey(Channel, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)