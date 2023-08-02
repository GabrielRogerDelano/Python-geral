# calcule o preço do aluguel de um carro considerando:
# R$60,00 por dia usado + R$0.15 por KM rodado

dias = int(input('quantos dias o carro ficaou alugado? '))
km = int(input('quantos KM rodados? '))

precoFinal = dias * 60 + km * 0.15

print('='*20)
print('O total a pagar é {:.2f}'.format(precoFinal))
print('='*20)
