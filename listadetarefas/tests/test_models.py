from django.test import TestCase
from listadetarefas.models import Tarefa

class TarefaModelTestCase(TestCase):

    def setUp(self):
        self.tarefa = Tarefa(
            titulo = 'Teste unitario',
            data_da_tarefa = '2023-10-26'
        )

    def test_verifica_atributos_do_programa(self):
        self.assertEqual(self.tarefa.titulo, 'Teste unitario')
        self.assertEqual(self.tarefa.data_da_tarefa, '2023-10-26')
        self.assertEqual(self.tarefa.status, 'P')
