class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)
    def set_nome(self, nome):
        self.nome = nome
    def set_ender(self, ender):
        self.ender = ender
    def get_nome(self):
        return self.nome
    def get_ender(self):
        return self.ender


pessoa1 = Pessoa("jose", "rua 1")
pessoa2 = Pessoa("eva", "rua 4")

print(f'Nome: {pessoa1.get_nome()}, Endereco: {pessoa1.get_ender()}')