from tkinter import *
from tkinter import ttk

def escreve() :
    print()

root = Tk()
root.geometry("300x150")
frm = ttk.Frame(root, padding=10, height=50)
frm.grid()
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=2)
ttk.Button(frm, text="Go", command=escreve).grid(column=1, row=0)
root.mainloop()