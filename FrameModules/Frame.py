from tkinter import *
from tkinter import ttk

class Frame:
    def __init__(self, f_busca, lista_nos):
        self.lista_nos = lista_nos
        self.f_busca = f_busca

    def buscar(self):
        origem = self.listaOrigem.get()
        destino = self.listaDestinos.get()
        print("De {} --para--> {}".format(origem, destino))
        self.f_busca(origem, destino)
        
    def run(self):
        app = Tk()
        app.title("Busca gulosa")
        app.geometry("160x180")
        app.configure(background="#03396c")
        self.listaOrigem = ttk.Combobox(app, values=self.lista_nos)
        self.listaDestinos = ttk.Combobox(app, values=self.lista_nos)
        emptyLabel = ttk.Label(app, text="", background="#03396c", font=("Arial", 10, "bold"), foreground="#f3f6f4")
        origemLabel = ttk.Label(app, text="Origem", background="#03396c", font=("Arial", 10, "bold"), foreground="#f3f6f4")
        destinoLabel = ttk.Label(app, text="Destino", background="#03396c", font=("Arial", 10, "bold"), foreground="#f3f6f4")
        btnSearch = Button(app, text="Buscar", command=self.buscar)
        btnSearch.config(
            activebackground="#005b96",
            activeforeground="#b3cde0",
            background="#6497b1",
            foreground="#f3f6f4",
            font=("Arial", 12, "bold"),
            cursor="hand2", 
            border=0
            )
        emptyLabel.grid(row=0, column=0, columnspan=4)

        origemLabel.grid(row=1, column=1, columnspan=2, sticky="e", padx=10)
        self.listaOrigem.grid(row=2, column=1, columnspan=3, padx=10)

        destinoLabel.grid(row=3, column=1, columnspan=2, sticky="e", padx=10)
        self.listaDestinos.grid(row=4, column=1, columnspan=3, padx=10)

        btnSearch.grid(row=5, column=1, columnspan=3, pady=20)
        app.mainloop()

#011f4b	(1,31,75)
#03396c	(3,57,108)
#005b96	(0,91,150)
#6497b1	(100,151,177)
#b3cde0	(179,205,224)