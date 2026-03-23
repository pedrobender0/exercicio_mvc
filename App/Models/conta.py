from Models.cliente import Cliente

class Conta:
    def __init__(self, numero: int, cliente: Cliente, saldo_inicial: float = 0.0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo_inicial