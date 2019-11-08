from django.db import models
from django.contrib.auth.models import User


class Conversa(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation_id = models.CharField(max_length=150, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.id_user.username