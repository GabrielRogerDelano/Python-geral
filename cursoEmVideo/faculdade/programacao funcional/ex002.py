lista = [0, 1, 1, 1, 2, 3, 5, 7, 8, 10, 13, 21, 34]

pares = filter(lambda item: item % 2 == 0, lista)

print(list(pares))
