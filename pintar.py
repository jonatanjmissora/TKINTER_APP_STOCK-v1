from tkinter import *

bg_gris = "#f2f2f2"

# ============= PINTAR de GRIS ====================
def c_rotura(tabla_datos, var):
	global lb_gris_c_roturas1, lb_gris_c_roturas2, lb_gris_c_roturas3, lb_gris_c_roturas4
	global lb_gris_c_roturas5, lb_gris_c_roturas6, lb_gris_c_roturas7, lb_gris_c_roturas8
	global lb_gris_c_roturas9, lb_gris_c_roturas10, lb_gris_c_roturas11

	if not var:
		lb_gris_c_roturas1=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_c_roturas1.place(x=80, y=0)
		lb_gris_c_roturas2=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_c_roturas2.place(x=80, y=44)
		lb_gris_c_roturas3=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_c_roturas3.place(x=80, y=88)
		lb_gris_c_roturas4=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_c_roturas4.place(x=80, y=132)
		lb_gris_c_roturas5=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_c_roturas5.place(x=80, y=176)
		lb_gris_c_roturas6=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_c_roturas6.place(x=80, y=220)
		lb_gris_c_roturas7=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_c_roturas7.place(x=80, y=264)
		lb_gris_c_roturas8=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_c_roturas8.place(x=80, y=308)
		lb_gris_c_roturas9=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_c_roturas9.place(x=80, y=352)
		lb_gris_c_roturas10=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_c_roturas10.place(x=80, y=396)
		lb_gris_c_roturas11=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_c_roturas11.place(x=80, y=440)
	else:
		lb_gris_c_roturas1.destroy()
		lb_gris_c_roturas2.destroy()
		lb_gris_c_roturas3.destroy()
		lb_gris_c_roturas4.destroy()
		lb_gris_c_roturas5.destroy()
		lb_gris_c_roturas6.destroy()
		lb_gris_c_roturas7.destroy()
		lb_gris_c_roturas8.destroy()
		lb_gris_c_roturas9.destroy()
		lb_gris_c_roturas10.destroy()
		lb_gris_c_roturas11.destroy()

def s_rotura(tabla_datos, var):
	global lb_gris_s_roturas1, lb_gris_s_roturas2, lb_gris_s_roturas3, lb_gris_s_roturas4
	global lb_gris_s_roturas5, lb_gris_s_roturas6, lb_gris_s_roturas7, lb_gris_s_roturas8
	global lb_gris_s_roturas9, lb_gris_s_roturas10, lb_gris_s_roturas11

	if not var:
		lb_gris_s_roturas1=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_s_roturas1.place(x=80, y=22)
		lb_gris_s_roturas2=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_s_roturas2.place(x=80, y=66)
		lb_gris_s_roturas3=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_s_roturas3.place(x=80, y=110)
		lb_gris_s_roturas4=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_s_roturas4.place(x=80, y=154)
		lb_gris_s_roturas5=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_s_roturas5.place(x=80, y=198)
		lb_gris_s_roturas6=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_s_roturas6.place(x=80, y=242)
		lb_gris_s_roturas7=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_s_roturas7.place(x=80, y=286)
		lb_gris_s_roturas8=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_s_roturas8.place(x=80, y=330)
		lb_gris_s_roturas9=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_s_roturas9.place(x=80, y=374)
		lb_gris_s_roturas10=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_s_roturas10.place(x=80, y=418)
		lb_gris_s_roturas11=Label(tabla_datos, bg=bg_gris, width=100, height=1)
		lb_gris_s_roturas11.place(x=80, y=462)
	else:
		lb_gris_s_roturas1.destroy()
		lb_gris_s_roturas2.destroy()
		lb_gris_s_roturas3.destroy()
		lb_gris_s_roturas4.destroy()
		lb_gris_s_roturas5.destroy()
		lb_gris_s_roturas6.destroy()
		lb_gris_s_roturas7.destroy()
		lb_gris_s_roturas8.destroy()
		lb_gris_s_roturas9.destroy()
		lb_gris_s_roturas10.destroy()
		lb_gris_s_roturas11.destroy()

def jean(tabla_datos, var):
	global lb_jean
	if not var:
		lb_jean=Label(tabla_datos, bg=bg_gris, width=9, height=50)
		lb_jean.place(x=80, y=0)
	else:
		lb_jean.destroy()

def blue(tabla_datos, var):
	global lb_blue
	if not var:
		lb_blue=Label(tabla_datos, bg=bg_gris, width=9, height=50)
		lb_blue.place(x=149, y=0)
	else:
		lb_blue.destroy()	

def gris(tabla_datos, var):
	global lb_gris
	if not var:
		lb_gris=Label(tabla_datos, bg=bg_gris, width=9, height=50)
		lb_gris.place(x=218, y=0)

	else:
		lb_gris.destroy()

def negro(tabla_datos, var):
	global lb_negro
	if not var:
		lb_negro=Label(tabla_datos, bg=bg_gris, width=9, height=50)
		lb_negro.place(x=287, y=0)
	else:
		lb_negro.destroy()

def oxido(tabla_datos, var):
	global lb_oxido
	if not var:
		lb_oxido=Label(tabla_datos, bg=bg_gris, width=9, height=50)
		lb_oxido.place(x=354, y=0)
	else:
		lb_oxido.destroy()



	

