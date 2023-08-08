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

    def extrato(self):
        print("Extrato:")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("Histórico de transações:")
        for transacao in self.historico:
            data = transacao["data"].strftime("%d/%m/%Y %H:%M:%S")
            valor = transacao["valor"]
            tipo = transacao["tipo"]
            print(f"{data} - {tipo}: R$ {valor:.2f}")


def main():
    conta = ContaBancaria()

    while True:
        print("\n1. Fazer depósito")
        print("2. Mostrar extrato")
        print("3. Sair")
        opcao = int(input("Escolha uma opção (1, 2 ou 3): "))

        if opcao == 1:
            valor = float(input("Digite o valor do depósito: "))
            if conta.depositar(valor):
                print("Depósito realizado com sucesso!")
        elif opcao == 2:
            conta.extrato()
        elif opcao == 3:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")


if __name__ == "__main__":
    main()
