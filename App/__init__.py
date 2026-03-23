import tkinter as tk
from Controllers.conta_controller import ContaController

if __name__ == "__main__":
    # Cria a janela principal do Tkinter
    root = tk.Tk()
    
    # Instancia o controlador passando a janela
    controller = ContaController(root)
    
    # Inicia o loop da interface gráfica
    root.mainloop()