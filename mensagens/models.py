from django.db import models
from core.models import Conversa


class Mensagem(models.Model):
    id_conversa = models.ForeignKey(Conversa, on_delete=models.CASCADE)
    texto = models.TextField(null=True, blank=True)
    autor = models.CharField(max_length=150, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.autor