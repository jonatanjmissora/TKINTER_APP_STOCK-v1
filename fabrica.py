from tkinter import *
from tkinter.ttk import Combobox
import datos_func
import pintar as pt

def fabricas_combo(event):
	pass

def fabrica_widgets(fabrica_frame):
	
	# ========== CONSTANTES =========================
	fnt12 = ("Arial", 12, "bold")
	fnt10 = ("Arial", 10, "bold")
	fabricantes=["TOXICO", "BLESS", "GENTE J", "TEXTIL M"]
	talles = [40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]
	
	# ========== FRAMES ===========================
	fabrica_seleccion = Frame(fabrica_frame, padx=10, pady=20)
	fabrica_seleccion.pack(fill=X)

	fabrica_checkbox = Frame(fabrica_frame)
	fabrica_checkbox.pack(fill=X)

	tabla_titulo = Frame(fabrica_frame, width=500, height=30)
	tabla_titulo.place(x=0, y=140)

	tabla_datos = Frame(fabrica_frame, width=500, height=500)
	tabla_datos.place(x=0, y=170, relwidth=1)

	# =========== LABEL Y COMBOBOX ==================
	Label(fabrica_seleccion, text="FABRICA:", font=fnt12).pack(side=LEFT)
	combo = Combobox(fabrica_seleccion, values=fabricantes, width=10, state="readonly", font=fnt12)
	combo.pack(side=LEFT)                             
	combo.current(0)                
	combo.bind("<<ComboboxSelected>>", fabricas_combo)
	combo.bind("<Return>", fabricas_combo)

	#============= CHECKBUTTONS =========================
	var_c_rotura = BooleanVar()
	var_s_rotura = BooleanVar()
	var_jean = BooleanVar()
	var_blue = BooleanVar()
	var_gris = BooleanVar()
	var_negro = BooleanVar()
	var_oxido = BooleanVar()
	
	ck_c_rotura = Checkbutton(fabrica_checkbox, text="c/rotura", justify=LEFT, variable=var_c_rotura,
								command=lambda:pt.c_rotura(tabla_datos, var_c_rotura.get()), font=fnt12)
	ck_s_rotura = Checkbutton(fabrica_checkbox, text="s/rotura", justify=LEFT, variable=var_s_rotura, 
								command=lambda:pt.s_rotura(tabla_datos, var_s_rotura.get()), font=fnt12)
	ck_jean = Checkbutton(fabrica_checkbox, text="jean", justify=LEFT, variable=var_jean, 
								command=lambda:pt.jean(tabla_datos, var_jean.get()), font=fnt12)
	ck_blue = Checkbutton(fabrica_checkbox, text="blueblack", justify=LEFT, variable=var_blue, 
								command=lambda:pt.blue(tabla_datos, var_blue.get()), font=fnt12)
	ck_gris = Checkbutton(fabrica_checkbox, text="gris", justify=LEFT, variable=var_gris, 
								command=lambda:pt.gris(tabla_datos, var_gris.get()), font=fnt12)
	ck_negro = Checkbutton(fabrica_checkbox, text="negro", justify=LEFT, variable=var_negro, 
								command=lambda:pt.negro(tabla_datos, var_negro.get()), font=fnt12)
	ck_oxido = Checkbutton(fabrica_checkbox, text="oxido", justify=LEFT, variable=var_oxido, 
								command=lambda:pt.oxido(tabla_datos, var_oxido.get()), font=fnt12)

	ck_c_rotura.select()
	ck_s_rotura.select()
	ck_jean.select()
	ck_blue.select()
	ck_gris.select()
	ck_negro.select()
	ck_oxido.select()

	ck_c_rotura.grid(row=0, column=0, sticky=W, padx=5)
	ck_s_rotura.grid(row=1, column=0, sticky=W, padx=5)
	ck_jean.grid(row=0, column=1, sticky=W, padx=5)  
	ck_blue.grid(row=1, column=1, sticky=W, padx=5)  
	ck_gris.grid(row=0, column=2, sticky=W, padx=5)  
	ck_negro.grid(row=1, column=2, sticky=W, padx=5)
	ck_oxido.grid(row=0, column=3, sticky=W, padx=5)  

	#============== TABLA TITULO ===========================
	Label(tabla_titulo, text ="TALLE             JEAN         BLUE        GRIS     NEGRO     OXIDO    ", font=fnt10).place(x=5, y=5)
	Frame(tabla_titulo, height=2, bd=1, bg="grey", relief=SUNKEN).place(x=0, y=25, relwidth=1)	

	# ============= TALLES ======================================
	for i in range(len(talles)):
		Label(tabla_datos, text=talles[i], font=("Arial", 25, "bold"), relief=GROOVE).grid(row=2*i, column=0, rowspan=2)
		Label(tabla_datos, text="c/rot", width=4, font=("Arial", 10, "bold"), relief=GROOVE).grid(row=2*i, column=1)		
		Label(tabla_datos, text="s/rot", width=4, font=("Arial", 10, "bold"), relief=GROOVE).grid(row=2*i+1, column=1)

	# ============= DATA ======================================
	datos_func.mostrar_datos(tabla_datos)