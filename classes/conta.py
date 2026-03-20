from classes.historico import Historico

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    def sacar(self, valor):
        if valor > self.saldo:
            print("\nSaldo insuficiente!")
            return False
        
        if valor > 0:
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([t for t in self.historico.transacoes if t["tipo"] == "Saque"])

        if valor > self.limite:
            print("Erro: O valor excede o limite.")
        elif numero_saques >= self.limite_saques:
            print("Erro: Limite de saques diários atingido.")
        else:
            return super().sacar(valor)
        return False