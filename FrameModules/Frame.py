from tkinter import *
from tkinter import ttk
from time import sleep

class Frame:
    def __init__(self, f_busca, lista_nos):
        self.lista_nos = lista_nos
        self.f_busca = f_busca
        self.line_text = 0
        self.app = None
        self.textArray = []

    def textCreate(self, text):
            label = ttk.Label(self.app, text=text, background="#03396c", font=("Arial", 10, "bold"), foreground="#f3f6f4")
            label.grid(row=self.line_text, column=4, columnspan=2, padx=15)
            self.textArray.append(label)
            # sleep(1)
            self.line_text += 1

    def clearText(self):
        self.line_text = 0
        for text in self.textArray:
            text.destroy()

    def buscar(self):
        origem = self.listaOrigem.get()
        destino = self.listaDestinos.get()
        print("De {} --para--> {}".format(origem, destino))
        self.clearText()
        self.f_busca(origem, destino, self.textCreate)
        

        
    def run(self):
        self.app = Tk()
        self.app.title("Busca gulosa")
        self.app.geometry("470x200")
        self.app.configure(background="#03396c")
        self.listaOrigem = ttk.Combobox(self.app, values=self.lista_nos)
        self.listaDestinos = ttk.Combobox(self.app, values=self.lista_nos)
        emptyLabel = ttk.Label(self.app, text="", background="#03396c", font=("Arial", 10, "bold"), foreground="#f3f6f4")
        origemLabel = ttk.Label(self.app, text="Origem", background="#03396c", font=("Arial", 10, "bold"), foreground="#f3f6f4")
        destinoLabel = ttk.Label(self.app, text="Destino", background="#03396c", font=("Arial", 10, "bold"), foreground="#f3f6f4")
        btnSearch = Button(self.app, text="Buscar", command=self.buscar)
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

        #Scrollbar
        
        self.app.mainloop()
        
        #Scrollbar

        

#011f4b	(1,31,75)
#03396c	(3,57,108)
#005b96	(0,91,150)
#6497b1	(100,151,177)
#b3cde0	(179,205,224)