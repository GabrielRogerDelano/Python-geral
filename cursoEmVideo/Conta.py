from datetime import datetime

class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append({"data": datetime.now(), "valor": valor, "tipo": "Depósito"})
            return True
        else:
            print("Valor inválido. O depósito deve ser maior que zero.")
            return False

    def sacar(self, valor):
        if (valor < self.saldo) and (valor > 0):
            self.saldo -= valor
            self.historico.append({"data": datetime.now(), "valor": -valor, "tipo": "Saque"})
            return True
        else:
            print("Valor inválido. O saque nao pode ser maior do que a conta nem menor que zero")

    def extrato(self):
        print("\033[0;33mExtrato:")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("Histórico de transações:")
        for transacao in self.historico:
            data = transacao["data"].strftime("%d/%m/%Y %H:%M:%S")
            valor = transacao["valor"]
            tipo = transacao["tipo"]
            print(f"{data} - {tipo}: R$ {valor:.2f}\033[m")


def main():
    conta = ContaBancaria()

    while True:
        print("\n1. Fazer depósito")
        print("2. Fazer saque")
        print("3. Mostrar extrato")
        print("4. Sair")
        opcao = int(input("\033[1;36mEscolha uma opção (1, 2, 3 ou 4): \033[m"))

        if opcao == 1:
            valor = float(input("Digite o valor do depósito: "))
            if conta.depositar(valor):
                print("\033[0;32mDepósito realizado com sucesso!\033[m")

        elif opcao == 2:
            valor = float(input("Digite o valor do saque: "))
            if conta.sacar(valor):
                print("\033[0;32mSaque realizado com sucesso!\033[m")

        elif opcao == 3:
            conta.extrato()

        elif opcao == 4:
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Escolha uma opção válida.")


if __name__ == "__main__":
    main()
