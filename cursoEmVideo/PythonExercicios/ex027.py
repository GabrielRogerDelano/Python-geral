# descubra o primeiro e ultimo nome de uma pessoa

n = input('Digite seu nome : \n').strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[-1]))
print('Seu ultimo nome é {}'.format(nome[len(nome) - 1]))

