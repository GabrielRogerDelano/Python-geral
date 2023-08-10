# implemente uma solucao para transfomar todos os nomes em mauisculo

veiculos = ['aviao', 'carro', 'navio', 'onibus']

maiuscula = lambda x: str.upper(x)

nomesMaiusculos = list(map(maiuscula, veiculos))

print(nomesMaiusculos)