from datetime import date


def data_valida(data_da_tarefa):
    return data_da_tarefa < date.today()

