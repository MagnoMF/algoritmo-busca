from tkinter import *

class Frame:
    # def __init__(self):
        
    def run(self):
        app = Tk()
        app.title("Busca gulosa")
        app.geometry("300x300")
        app.configure(background="#03396c")
        btnSearch = Button(app, text="Buscar")
        btnSearch.place(x=150-35, y=5, width=70, height=30, bordermode="outside")
        #simple button
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
        langs = ('Java', 'C#', 'C', 'C++', 'Python', 'Go', 'JavaScript', 'PHP', 'Swift')
        
        listaDestinos = Listbox(app, listvariable=langs).place(x=150-35, y=35, width=70, height=30, bordermode="outside")
        # destiny = Entry(app)
        # destiny.place(x=5, y=5, width=200, height=20, bordermode='outside')
        app.mainloop()

#011f4b	(1,31,75)
#03396c	(3,57,108)
#005b96	(0,91,150)
#6497b1	(100,151,177)
#b3cde0	(179,205,224)