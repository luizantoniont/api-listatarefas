from django.contrib import admin
from listadetarefas.models import Tarefa

class Tarefas(admin.ModelAdmin):

    list_display = ('id', 'titulo', 'data_da_tarefa', 'hora_da_tarefa')
    list_display_links = ('titulo',)
    search_fields = ('data_da_tarefa', 'status',)
    list_per_page = 10
    ordering = ('data_da_tarefa',)

admin.site.register(Tarefa, Tarefas)
