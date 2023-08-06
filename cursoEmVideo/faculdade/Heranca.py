class ClasseSomaMultiplica:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def multiplicar(self):
        return self.a * self.b


class Derivada(ClasseSomaMultiplica):
    def subtracao(self):
        return self.a - self.b

    def divisao(self):
        return self.a / self.b


d = Derivada(27, 81)
print(f'A soma de {d.a} + {d.b} = {d.soma()}')
print(issubclass(Derivada, ClasseSomaMultiplica))
