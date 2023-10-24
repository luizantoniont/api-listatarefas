from datetime import date


def data_valida(data_da_tarefa):
    return data_da_tarefa < date.today()
#def hora_valida(hora_da_tarefa):
    #return hora_da_tarefa < datetime.time.now()