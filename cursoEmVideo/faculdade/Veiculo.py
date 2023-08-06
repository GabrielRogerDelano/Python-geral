class Veiculo:
    def __init__(self, nome, velocidade_maxima, quilometros_litro):
        self.nome = nome
        self.velocidade_maxima = velocidade_maxima
        self.quilometros_litro = quilometros_litro

    def capacidade_assentos(self, capacidade):
        print('A capacidade de assentos é igual a {}'.format(capacidade))

    def informacaoes(self):
        print('Nome = {} \nvelocidade máxima = {} \nquilometros percorridos por litro = {}'
              .format(self.nome, self.velocidade_maxima, self.quilometros_litro))


class Onibus(Veiculo):
    def quantidade_de_assentos(self, capacidade =  70):
        return super().capacidade_assentos(capacidade)


onibus_escolar = Veiculo('Scania', 110, 8)
onibus_escolar.informacaoes()
onibus_escolar.capacidade_assentos(34)

#carro = Veiculo('onix prata', 120, 13)
#carro.informacaoes()