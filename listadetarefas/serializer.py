from rest_framework import serializers
from listadetarefas.models import Tarefa
from listadetarefas.validators import *


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'

    def validate(self, data):
        if data_valida(data['data_da_tarefa']):
            raise serializers.ValidationError({'data_da_tarefa':"A data não pode ser anterior a data atual"})
        #if hora_valida(data['hora_da_tarefa']):
            #raise serializers.ValidationError({'hora_da_tarefa':"A #hora da tarefa não pode ser anterior a hora atual"})
        return data
