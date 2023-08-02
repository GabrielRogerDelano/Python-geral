# programa que calcula a area de uma parede e diz quantos litros usar pintá-la

largura = float(input('Digite a largura da parede em metros\n'))
comprimento = float(input('Digite o comprimento da parede metros\n'))

area = largura * comprimento
# considerando que 1L rende 2m quadrados
litros = area / 2

print('='*20)
print('A parede tem {}m quadrados e será necessário {} litros de pinta'.format(area, litros))
print('='*20)
