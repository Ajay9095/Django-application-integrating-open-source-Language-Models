from django.db import models

# Create your models here.
from djongo import models

class ChatHistory(models.Model):
    user_id = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    user_input = models.TextField()
    model_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.model_name} - {self.timestamp}"
