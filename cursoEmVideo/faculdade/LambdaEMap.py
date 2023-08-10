lista = [1, 2, 3, 4, 5]

# Labmda é uma funcao anonima do python e sua estrutura é : lambda a,b: a * b

# Map executa um funcao nos parametros que sao passados. Exemplo;map(função, iterável1, iterável2) ou map(soma, lista).
# E se aplica a todos os itens dentro de list
nova_lista = map(lambda item: item * 3, lista)


def main():
    print(list(nova_lista))


if __name__ == '__main__':
    main()
