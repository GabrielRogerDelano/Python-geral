# multa de carro

velocidadeAtual = float(input("Digite um a velocidade atual : "))

if velocidadeAtual > 60:
    print("\033[1;31mMultado, excedeu o limite de velocidade de 60km/h")
    multa = (velocidadeAtual - 59) * 7
    print("\033[1;31mtera que pagar R${:.2f}".format(multa))
else:
    print("\033[1;32mtenha um bom dia")
