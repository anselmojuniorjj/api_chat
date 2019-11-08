from rest_framework.serializers import ModelSerializer
from mensagens.models import Mensagem


class MensagemSerializer(ModelSerializer):
    class Meta:
        model = Mensagem
        fields = ('id', 'id_conversa', 'texto', 'autor', 'date')