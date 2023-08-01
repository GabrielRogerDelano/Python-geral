# conversor de moedas

pesoDolar = 3.27

reais = float(input('Digite quantos reais você têm\nR$'))
dolares = reais / pesoDolar

print('='*20)
print('Você têm ${:.2f}'.format(dolares))
print('='*20)
