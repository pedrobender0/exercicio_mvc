import tkinter as tk
from Controllers.conta_controller import ContaController

if __name__ == "__main__":
    root = tk.Tk()
    
    controller = ContaController(root)
    
    root.mainloop()