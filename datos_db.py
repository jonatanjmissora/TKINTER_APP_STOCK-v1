import sqlite3


def crear_tabla():
  conn = sqlite3.connect("datos_db.db")
  c = conn.cursor()

  c.execute("""CREATE TABLE datos_tb (
        jean int,
        blue int,
        gris int,
        negro int,
        oxido int,)
        """)
  conn.commit()
  conn.close()


def insertar_todos(lista):
  conn = sqlite3.connect("datos_db.db")
  c = conn.cursor()
  c.executemany("INSERT INTO datos_tb VALUES (?,?,?,?,?)", lista)
  conn.commit()
  conn.close()


def mostrar_todos():
  conn = sqlite3.connect("datos_db.db")
  c = conn.cursor()
  c.execute("SELECT * FROM datos_tb")
  [print(row) for row in c.fetchall()]
  conn.commit()
  conn.close()

def obtener_un_renglon(indice):
  conn = sqlite3.connect("datos_db.db")
  c = conn.cursor()
  c.execute("SELECT * FROM datos_tb WHERE rowid=?", (indice, ))
  row = c.fetchone()
  conn.commit()
  conn.close()
  return row

def modificar_renglon(indice, renglon)

#datos = [(15, 20, 17, 15, 18), (3, 4, 2, 3, 2), (5, 13, 5, 9, 5),
#         (2, 10, 8, 2, 8), (1, 39, 6, 7, 1), (5, 10, 8, 5, 3),
#         (5, 20, 7, 5, 8), (3, 14, 2, 13, 2), (5, 13, 5, 9, 5),
#         (2, 10, 8, 2, 8), (1, 39, 6, 7, 1), (5, 10, 8, 5, 3),
#         (5, 20, 7, 5, 8), (3, 14, 2, 3, 2), (5, 13, 5, 9, 5),
#         (2, 10, 8, 2, 8), (1, 39, 6, 7, 11), (5, 10, 8, 5, 3),
#         (5, 20, 7, 5, 8), (3, 14, 2, 3, 2), (5, 13, 5, 19, 5),
#         (2, 10, 8, 2, 8),]

#crear_tabla()
#insertar_todos(datos)
#mostrar_todos()