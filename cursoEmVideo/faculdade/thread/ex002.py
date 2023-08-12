# inicie um thread, espere 2s e informe o inicio e final da thread

from threading import Thread
import time


def tarefa(tempo_espera, nome_tarefa):
    print("Iniciando a tarefa ", nome_tarefa)
    time.sleep(tempo_espera)
    print("conclusao da tarefa ", nome_tarefa)


tarefa1 = Thread(target=tarefa, args=(3, 'A'))
tarefa2 = Thread(target=tarefa, args=(2, ' B'))

tarefa1.start()
tarefa2.start()

tarefa1.join()# espera ate completar a execucao da thread 1
tarefa2.join()# espera ate completar a execucao da thread 2

print('Execucao foi concluida!')
