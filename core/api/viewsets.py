from rest_framework.viewsets import ModelViewSet
from core.models import Conversa
from .serializers import ConversaSerializer


class ConversaViewSet(ModelViewSet):
    queryset = Conversa.objects.all()
    serializer_class = ConversaSerializer