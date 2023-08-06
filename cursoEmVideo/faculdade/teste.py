class Banco:
    def __init__(self, codigo,nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adicionaconta(self,contacliente):
        self.contas.append(contacliente)


pessoa = Banco(123, 'Santander')

print(pessoa.codigo)
print(pessoa.nome)
print(pessoa.contas)

pessoa.adicionaconta('e')
pessoa.adicionaconta(1)

print(pessoa.codigo)
print(pessoa.nome)
print(pessoa.contas)
