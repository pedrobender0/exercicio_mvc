import tkinter as tk
from tkinter import messagebox

class View:
    def __init__(self, root, comando_salvar):
        self.root = root
        self.root.title("Sistema Bancário")
        self.root.geometry("350x300")
        
        self.comando_salvar = comando_salvar

        tk.Label(root, text="=== CADASTRO DE CONTA ===", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Label(root, text="Nome do Cliente:").pack()
        self.entry_nome = tk.Entry(root, width=30)
        self.entry_nome.pack(pady=5)

        tk.Label(root, text="CPF do Cliente:").pack()
        self.entry_cpf = tk.Entry(root, width=30)
        self.entry_cpf.pack(pady=5)

        tk.Label(root, text="Saldo Inicial (R$):").pack()
        self.entry_saldo = tk.Entry(root, width=30)
        self.entry_saldo.pack(pady=5)

        tk.Button(root, text="Criar Conta", command=self.enviar_dados, bg="lightblue").pack(pady=15)

    def enviar_dados(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        saldo_texto = self.entry_saldo.get()

        if not nome or not cpf:
            messagebox.showerror("Erro", "Nome e CPF são obrigatórios!")
            return

        try:
            saldo_inicial = float(saldo_texto) if saldo_texto else 0.0
        except ValueError:
            messagebox.showwarning("Aviso", "Valor inválido! O saldo inicial será R$ 0.00.")
            saldo_inicial = 0.0
            
        self.comando_salvar(nome, cpf, saldo_inicial)

    def exibir_dados_conta(self, conta):
        mensagem = (
            f"Conta criada com sucesso!\n\n"
            f"Número da Conta: {conta.numero}\n"
            f"Cliente: {conta.cliente.nome}\n"
            f"CPF: {conta.cliente.cpf}\n"
            f"Saldo Atual: R$ {conta.saldo:.2f}"
        )
        messagebox.showinfo("Sucesso", mensagem)
        
        self.entry_nome.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_saldo.delete(0, tk.END)