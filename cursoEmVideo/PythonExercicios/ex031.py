distancia = float(input("qual é a distancia da sua viagem : "))

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print("A sua viagem de {} custará R${:.2f}".format(distancia, preco))


