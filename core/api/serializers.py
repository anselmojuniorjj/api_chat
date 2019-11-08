from rest_framework.serializers import ModelSerializer
from core.models import Conversa


class ConversaSerializer(ModelSerializer):
    class Meta:
        model = Conversa
        fields = ('id', 'id_user', 'conversation_id', 'date')