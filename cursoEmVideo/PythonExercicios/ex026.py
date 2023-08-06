# Descubra quando comeca o primeiro a e o ultimo aparecem

frase = input("Digite uma frase").upper().strip()

print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posicao  {} '.format(frase.find('A') + 1))
print('e a ultima na posicao {}'.format(frase.rfind('A') + 1))
