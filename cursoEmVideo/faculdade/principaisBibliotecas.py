# Usado para operações matemáticas.
import math

'''
algumas funcoes:

sqrt(x)	Raiz quadrada de x
ceil(x)	Menor inteiro maior ou igual a x
floor(x)	Maior inteiro menor ou igual a x
cos(x)	Cosseno de x
sin(x)	Seno de x
log(x, b) Logaritmo de x na base b


'''

# Usado para gerar números pseudoaleatórios
import random

'''

Para numeros reais:
random()	Número de ponto flutuante no intervalo (00,0, 1,0)
uniform(a, b)	Número de ponto flutuante N tal que a ≤ N ≤ b
gauss(mu, sigma)	Distribuição gaussiana. mu é a média e sigma é o desvio padrão.
normalvariate(mu, sigma)	Distribuição gaussiana. mu é a média e sigma é o desvio padrão.

Para numeros inteiros:
randrange(stop)	Um elemento selecionado aleatório de range(start, stop, step), mas sem construir um objeto range.
randrange(start, stop, [step])	
randint(a, b)	Número inteiro N tal que a ≤ N ≤ b

Para sequencias:
choice(seq)	Elemento aleatório de uma sequência não vazia seq.
shuffle(x[, random])	Embaralha a sequência x no lugar.
sample(pop, k)	Uma sequência de tamanho k de elementos escolhidos da população pop, sem repetição. Usada para amostragem sem substituição.
'''
# Usado para permitir envio de e-mails
import smtplib

# Usado para implementar contadores temporais.
import time
'''

time()	        Número de segundos passados desde o início da contagem (epoch). Por padrão, o início é 00:00:00 do dia 1 de janeiro de 1970.
ctime(segundos)	Uma string representando o horário local, calculado a partir do número de segundos passado como parâmetro.
gmtime(segundos)	Converte o número de segundos em um objeto struct_time descrito a seguir.
localtime(segundos)	Semelhante à gmtime(), mas converte para o horário local.
sleep(segundos)	A função suspende a execução por determinado número de segundos

'''

# Usado para desenvolver interfaces gráficas.
import tkinter
