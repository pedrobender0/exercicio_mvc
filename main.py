from classes.cliente import PessoaFisica
from classes.conta import ContaCorrente
from classes.transacao import Deposito, Saque


cliente = PessoaFisica("123.456.789-00", "Pedro", "25/09/2006", "Rua X, 123")


conta = ContaCorrente(numero=1, cliente=cliente)
cliente.adicionar_conta(conta)


deposito = Deposito(1000.0)
cliente.realizar_transacao(conta, deposito)

saque = Saque(200.0)
cliente.realizar_transacao(conta, saque)


print(f"Cliente: {cliente.nome}")
print(f"Saldo atual: R$ {conta.saldo:.2f}")
print("Histórico:")
for t in conta.historico.transacoes:
    print(f"- {t['tipo']}: R$ {t['valor']}")