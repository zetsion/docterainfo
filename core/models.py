from django.db import models

# Create your models here.
# contact/models.py or wherever your model is

from django.db import models
from django.contrib.auth.models import User

class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    if self.user:
        return f"Message from {self.name or self.user.username}"
    return f"Message from {self.name or 'Anonymous'}"

