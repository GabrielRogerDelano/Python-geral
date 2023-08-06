# jogo de adivinhacao entre 0 e 5
from random import randint

numSorteado = randint(0, 5)


for i in range(2, -1, -1):

    numEscolhido = int(input("Digite um numero entre 0 e 5 : "))

    if numEscolhido == numSorteado:
        print("Voce acertou o numero sorteado")
        break
    else:
        print("\nVoce errou, voce tem mais {} tentativas ".format(i))
