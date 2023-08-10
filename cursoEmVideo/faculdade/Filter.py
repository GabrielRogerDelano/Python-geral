# O filtro é realizado utilizando uma função, que deve ser capaz de retornar
# true ou false (verdadeiro ou falso) para cada elemento do iterável.
# sua sintaxe é filter(funcao, iteravel)

lista = [1, 2, 3, 4, 5]

nova_lista = filter(lambda item: item % 2 != 0, lista)

def main():
    print("Somente numeros impares : ", list(nova_lista))


if __name__ == "__main__":
    main()
