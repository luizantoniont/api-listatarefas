from django.db import models

class Tarefa(models.Model):

    STATUS = (
        ('P', 'Pendente'),
        ('A', 'Em andamento'), 
        ('C', 'Concluída')
    )

    titulo = models.CharField(max_length=255)
    data_da_tarefa = models.DateField()
    hora_da_tarefa = models.TimeField()
    descricao = models.TextField(max_length=500)
    status = models.CharField(max_length=1, choices=STATUS, default='P')

    def __str__(self):
        return self.titulo