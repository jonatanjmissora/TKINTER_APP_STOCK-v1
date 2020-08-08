from tkinter import *
from tkinter.ttk import Combobox
import datos_func

def fabricas_combo(event):
	pass

def seleccion_talle(event):
	global talle_txt, combo_talle
	talle_txt.set(combo_talle.get())

def cambiar_datos():
	global en1, en2, en3, en4, en5, en6, en7, en8, en9, en10
	global tabla_datos, talle_txt
	cambio1=(en1.get(), en2.get(), en3.get(), en4.get(), en5.get())
	cambio2=(en6.get(), en7.get(), en8.get(), en9.get(), en10.get())
	datos_func.modificar_datos(int(talle_txt.get()), cambio1, cambio2)

	# borrar entries
	en1.delete(0, END)
	en2.delete(0, END)
	en3.delete(0, END)
	en4.delete(0, END)
	en5.delete(0, END)
	en6.delete(0, END)
	en7.delete(0, END)
	en8.delete(0, END)
	en9.delete(0, END)
	en10.delete(0, END)
	
def cargar_widgets(cargar_frame):

	global tabla_datos, talle_txt, combo_talle
	global en1, en2, en3, en4, en5, en6, en7, en8, en9, en10
	# ========== CONSTANTES =========================
	fnt12 = ("Arial", 12, "bold")
	fnt10 = ("Arial", 10, "bold")
	fabricantes=["TOXICO", "BLESS", "GENTE J", "TEXTIL M"]
	talles = [40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]

	# ========== FRAMES ===========================
	fabrica_seleccion = Frame(cargar_frame, padx=10, pady=20)
	fabrica_seleccion.pack(fill=X)

	talles_seleccion = Frame(cargar_frame)
	talles_seleccion.pack(fill=X)

	tabla_titulo = Frame(cargar_frame, height=35, width=500)
	tabla_titulo.place(x=0, y=110)

	tabla_datos = Frame(cargar_frame, width=394, height=500)
	tabla_datos.place(x=0, y=140, relwidth=1)

	#============= FABRICAS ============================
	Label(fabrica_seleccion, text="FABRICA:", font=fnt12).pack(side=LEFT)

	combo_fb = Combobox(fabrica_seleccion, values=fabricantes, width=10, state="readonly", font=fnt12)
	combo_fb.pack(side=LEFT)                             
	combo_fb.current(0)                
	combo_fb.bind("<<ComboboxSelected>>", fabricas_combo)
	combo_fb.bind("<Return>", fabricas_combo) 

	#============== TALLE A CARGAR ===========================
	Label(talles_seleccion, text="TALLE:", font=fnt12).pack(side=LEFT)
	talles = ["40", "42", "44", "46", "48", "50", "52", "54", "56", "58", "60"]
	combo_talle = Combobox(talles_seleccion, values=talles, width=5, state="readonly", font=fnt12)
	combo_talle.pack(side=LEFT)                             
	combo_talle.current(0)                
	combo_talle.bind("<<ComboboxSelected>>", seleccion_talle)
	combo_talle.bind("<Return>", seleccion_talle) 

	#============== TITULO LISTADO ===========================
	Label(tabla_titulo, text ="TALLE           JEAN      BLUE        GRIS      NEGRO     OXIDO    ", font=fnt10).place(x=5, y=5)
	Frame(tabla_titulo, height=2, bd=1, bg="grey", relief=SUNKEN).place(x=0, y=25, relwidth=1)	

	# ============= TALLE A CARGAR =============================
	talle_txt = StringVar()
	talle_txt.set("40")
	talle_lb = Label(tabla_datos, textvariable=talle_txt, font=("Arial", 25, "bold"), relief=GROOVE)
	talle_lb.grid(row=0, column=0, rowspan=2)
	Label(tabla_datos, text="c/rot", width=4, font=("Arial", 10, "bold"), relief=GROOVE).grid(row=0, column=1)		
	Label(tabla_datos, text="s/rot", width=4, font=("Arial", 10, "bold"), relief=GROOVE).grid(row=1, column=1)

	# ============= DATOS A CARGAR =============================
	en1=Entry(tabla_datos, width=8, justify=CENTER)
	en1.grid(row=0, column=2)
	en2=Entry(tabla_datos, width=8, justify=CENTER)
	en2.grid(row=0, column=3)
	en3=Entry(tabla_datos, width=8, justify=CENTER)
	en3.grid(row=0, column=4)
	en4=Entry(tabla_datos, width=9, justify=CENTER)
	en4.grid(row=0, column=5)
	en5=Entry(tabla_datos, width=9, justify=CENTER)
	en5.grid(row=0, column=6)
	en6=Entry(tabla_datos, width=8, justify=CENTER)
	en6.grid(row=1, column=2)
	en7=Entry(tabla_datos, width=8, justify=CENTER)
	en7.grid(row=1, column=3)
	en8=Entry(tabla_datos, width=8, justify=CENTER)
	en8.grid(row=1, column=4)
	en9=Entry(tabla_datos, width=9, justify=CENTER)
	en9.grid(row=1, column=5)
	en10=Entry(tabla_datos, width=9, justify=CENTER)
	en10.grid(row=1, column=6)

	Label(tabla_datos).grid(row=2, column=0)
	but1=Button(tabla_datos, text="CARGAR", command=cambiar_datos)
	but1.grid(row=3, column=3)


	
	


