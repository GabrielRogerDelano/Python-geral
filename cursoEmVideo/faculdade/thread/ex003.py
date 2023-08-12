# inicie um thread, espere 2s e informe o inicio e final da thread

from threading import Thread
from math import pow
from time import sleep


def quadrado(tempo_espera, num):
    print('Quadrado: ', (pow(num, 2)))
    sleep(tempo_espera)
    print('Conclusao da funcao quadrado ')


def cubo(tempo_espera, num):
    print('Cubo: ', (pow(num, 3)))
    sleep(tempo_espera)
    print('Conclusao da funcao cubo ')


quadrado = Thread(target=quadrado, args=(2, 2))
cubo = Thread(target=cubo, args=(3, 2))

quadrado.start()
cubo.start()


quadrado.join()  # espera ate completar a execucao da thread 1


cubo.join()  # espera ate completar a execucao da thread 2

print('Execucao foi concluida!')
