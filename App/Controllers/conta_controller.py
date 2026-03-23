from Models.cliente import Cliente
from Models.conta import Conta
from Models.bancodados import BancoDados
from Views.main import View

class ContaController:
    def __init__(self, root):
        self.banco_dados = BancoDados()
        self.view = View(root, self.criar_conta)
        self.numero_conta_atual = 1001

    def criar_conta(self, nome, cpf, saldo_inicial):
        cliente = Cliente(nome=nome, cpf=cpf)

        conta = Conta(numero=self.numero_conta_atual, cliente=cliente, saldo_inicial=saldo_inicial)
        self.numero_conta_atual += 1

        self.banco_dados.salvar_conta(conta)

        self.view.exibir_dados_conta(conta)