import datetime
import ContasClientesExtrato
from Extrato import Extrato


class Conta:
    def __init__(self,clientes,numero,saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.sataAbertura = datetime.satetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.trasacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today ()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True

    def transfereValor(self, contadestino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return "Transferencia Realizada"

    def gerarsaldo(self):
        print(f"numero: {self.numero}\n saldo:{self.saldo}")


cliente1 = Cliente("123", "Joao", "Rua X")
cliente2 = Cliente("456","Maria","Rua W")

conta1 = Conta([cliente1, cliente2], 1, 2000)

conta1.depositar(1000)
conta1.sacar(1500)
