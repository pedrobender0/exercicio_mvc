from Models.conta import Conta

class BancoDados:
    def __init__(self):
        self.contas = []

    def salvar_conta(self, conta: Conta):
        self.contas.append(conta)

    def listar_contas(self):
        return self.contas