from App.Models.cliente import PessoaFisica
from App.Models.conta import ContaCorrente
from App.Models.transacao import Deposito, Saque
import tkinter as tk


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

#Criação janela
def abrir_janela():
    janela_criarconta = tk.Toplevel()
    janela_criarconta.title("Sistema Bancário")
    janela_criarconta.geometry("300x300")
    label_nome = tk.Label(janela_criarconta, text = "Nome")
    label_nome.grid(row = 0, column = 0 )
    botao_voltar = tk.Button(janela_criarconta, text = 'Enviar informações', command = janela_criarconta.destroy)
    botao_voltar.grid(row=1, column=0)

janela_inicial = tk.Tk()
janela_inicial.title("Sistema Bancário")
janela_inicial.geometry("300x300")
botao = tk.Button(janela_inicial, text = 'Criar conta', command = abrir_janela)
botao.grid(row = 0, column = 0)


janela_inicial.mainloop()