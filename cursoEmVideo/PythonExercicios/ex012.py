# lê preço e calcula desconto

precoDado = float(input('Digite o preco do produto\nR$'))

desconto = 1/20
precoFinal = precoDado * (1 - desconto)

print('='*20)
print("Valor sem desconto = {}\nValor do desconto = {} ou {}%\nValor Final = {}"
      .format(precoDado, desconto, desconto * 100, precoFinal))
print('='*20)
