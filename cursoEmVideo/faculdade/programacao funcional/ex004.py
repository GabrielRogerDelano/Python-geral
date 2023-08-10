lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def soma(numeros):
    if not numeros:
        return 0

    primeiro = numeros[0]
    resto = numeros[1:]
    return primeiro + soma(resto)


print(soma(lista))
print(lista)
