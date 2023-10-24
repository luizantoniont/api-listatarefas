from rest_framework import viewsets, filters
from listadetarefas.models import Tarefa
from listadetarefas.serializer import TarefaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend




class TarefasViewSet(viewsets.ModelViewSet):
    """Exibir todas as tarefas"""
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['titulo','data_da_tarefa']
    search_fields = ['titulo','data_da_tarefa']
    filterset_fields = ['status']







