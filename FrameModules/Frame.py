from tkinter import *
from tkinter import ttk

class Frame:
    def __init__(self):
        self.lista_nos = ('Java', 'C#', 'C', 'C++', 'Python', 'Go', 'JavaScript', 'PHP', 'Swift')

    def buscar(self):
        destino = self.listaOrigem.get()
        origem = self.listaDestinos.get()
        print("De {} --para--> {}".format(origem, destino))
        
    def run(self):
        app = Tk()
        app.title("Busca gulosa")
        app.geometry("300x300")
        app.configure(background="#03396c")
       
        self.listaOrigem = ttk.Combobox(app, values=self.lista_nos)
        self.listaDestinos = ttk.Combobox(app, values=self.lista_nos)
        origemLabel = ttk.Label(app, text="Origem")
        origemLabel.pack()
        self.listaDestinos.place(x=150-75, y=5, width=150, height=30, bordermode="outside")
        self.listaOrigem.place(x=150-75, y=20+30, width=150, height=30, bordermode="outside")
        btnSearch = Button(app, text="Buscar", command=self.buscar)
        btnSearch.place(x=150-35, y=90, width=70, height=30, bordermode="outside")
        btnSearch.config(
            activebackground="#005b96",
            activeforeground="#b3cde0",
            background="#6497b1",
            foreground="#f3f6f4",
            font=("Arial", 12, "bold"),
            pady=20,
            cursor="hand2", 
            border=0
            )
        app.mainloop()

#011f4b	(1,31,75)
#03396c	(3,57,108)
#005b96	(0,91,150)
#6497b1	(100,151,177)
#b3cde0	(179,205,224)