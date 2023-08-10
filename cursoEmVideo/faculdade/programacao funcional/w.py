# Na programacao funcional procura-se utilidar dos daos sem muda-los. Como no exemplo

lista = [2, 1, 3, 2, 1, 2]# dados


def soma(numeros):
    if not numeros:
        return 0
    primeiro = numeros[0]
    resto = numeros[1:]
    return primeiro + soma(resto)


print(soma(lista))# manda uma a lista para a funcao
print(lista)# os dados continuam inalterados


# No exemplo a seguir mudamos a lista
carros = ['ferrari']
carros.append('fiat uno')
print(carros)

# Nesse salvamos em outra lista
outroCarro = carros + ['celta']
print(outroCarro)
