# inicie um thread, espere 2s e informe o inicio e final da thread

from threading import Thread
import time


def tarefa(tempo_espera, mensagem):
    print("\nIniciando a tarefa ", mensagem)
    time.sleep(tempo_espera)
    print("conclusao da tarefa ", mensagem)


thread = Thread(target=tarefa, args=(2, 'thread em excucao'))
thread.start()
print('\nAguardadno pela execucao da thread...')
thread.join()
print('Execucao foi concluida!')
