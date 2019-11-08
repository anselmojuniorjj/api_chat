from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from mensagens.models import Mensagem
from .serializers import MensagemSerializer


class MensagemViewSet(ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer

    # habilita buscas
    filter_backends = [DjangoFilterBackend,]
    # search_fields = ['id_conversa', 'autor', 'date']
    filter_fields = ('id_conversa', 'autor', 'date')

    # altera o comportamento padrão(busca por id)
    # lookup_field = 'id_conversa'

    def get_queryset(self):
        id_conversa = self.request.query_params.get('id_conversa', None)
        autor = self.request.query_params.get('autor', None)
        date = self.request.query_params.get('date', None)
        queryset = Mensagem.objects.all()

        if id_conversa:
            queryset = queryset.filter(id_conversa=id_conversa)

        if autor:
            queryset = queryset.filter(autor__iexact=autor)

        if date:
            queryset = queryset.filter(date__iexact=date)

        return queryset