lista_numeros = [ 9.54321, 3.54321, 21.54321, 87.54321]
lista_precisao = [ 2, 2, 3, 3]

arredondar = lambda x, y: round(x, y)

nova_lista = list(map(arredondar, lista_numeros, lista_precisao))

print(nova_lista)
