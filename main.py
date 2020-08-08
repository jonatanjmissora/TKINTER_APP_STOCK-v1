from tkinter.ttk import *
from tkinter import *
import fabrica as fb
import cargar as cg

root = Tk()
root.geometry("500x800+10+0")

note = ttk.Notebook(root, width=420, height=660, padding=3)
note.pack()

fabrica_frame = Frame(note, bd=2, relief="sunken")
note.add(fabrica_frame, text="FABRICA")
fb.fabrica_widgets(fabrica_frame)

buscar_frame = Frame(note, bd=2, relief="sunken")
note.add(buscar_frame, text="BUSCAR")

cargar_frame = Frame(note, bd=2, relief="sunken")
note.add(cargar_frame, text="CARGAR")
cg.cargar_widgets(cargar_frame)

root.mainloop()


