from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Welcome(models.Model):
    readonly_field = models.CharField(max_length=100, editable=False)

    def __str__(self):
        return self.text