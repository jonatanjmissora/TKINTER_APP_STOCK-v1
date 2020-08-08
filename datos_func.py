from tkinter import *
import datos_db

#============= CONSTANTES =================
talles = [40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]

#============= FUNCIONES PARA FABRICA ===============  

def mostrar_datos(tabla_datos):
  lista_datos = datos_a_txt()
  datos_Text = Text(tabla_datos, font=("Arial", 14))
  datos_Text.place(x=80, y=0)
  for i in range(0, 22):
    datos_Text.insert(str(i+1)+".0", lista_datos[i])
  datos_Text.configure(state='disabled')

  # lineas divisorias de la tabla
  for i in range(len(talles)):
    Frame(tabla_datos, height=2, bd=1, bg="light grey", relief=SUNKEN).grid(row=2*i+1, column=3, ipadx=200, sticky=N)
    Frame(tabla_datos, height=3, bd=1, bg="black", relief=SUNKEN).grid(row=2*i+2, column=3, ipadx=200, sticky=N)
  for i in range(4):
    sep=ttk.Separator(tabla_datos, orient=VERTICAL).place(x=148+i*69, y=0, height=500)


def datos_a_txt():
  # paso los datos de la tabla a formato texto
  correcion_espacio = " "
  lista_datos = []
  
  for i in range(1, 23):
    row = datos_db.obtener_un_renglon(i)
    num = str(row[0])
    if len(num) > 1:
        correcion_espacio = ""
    else:
        correcion_espacio = " "
    renglon = "     " + correcion_espacio + num
    
    #cargo el resto de los datos del renglon y los idento
    for j in range(1, 5):
      num = str(row[j])
      if len(num) > 1:
        correcion_espacio = ""
      else:
        correcion_espacio = "  "
      renglon += " "*9 + correcion_espacio + num
    renglon += "\n"
    
    #cargo el renglon
    lista_datos.append(renglon)
  
  return lista_datos                  



#============= FUNCIONES PARA CARGAR ===============

def modificar_datos(talle, li1, li2):
  datos = 
  print(datos)
  indice = talles.index(talle)*2
  datos[indice]=li1
  datos[indice+1]=li2
  print(datos[indice])
  print(datos[indice+1])
