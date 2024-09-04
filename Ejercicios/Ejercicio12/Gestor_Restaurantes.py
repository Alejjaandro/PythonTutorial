from tkinter import *

from comidas import check_button_comidas, texto_comidas, precios_comidas
from bebidas import check_button_bebidas, texto_bebidas, precios_bebidas
from postres import check_button_postres, texto_postres, precios_postres
from precios import generar_recibo, generar_calculadora

# Iniciamos la ventana
aplicacion = Tk()

# Tamaño de la ventana
ventana_width = 1500
ventana_height = 600
pantalla_x = 0
pantalla_y = 0
aplicacion.geometry(f"{ventana_width}x{ventana_height}+{pantalla_x}+{pantalla_y}")
# Evitar que la ventana se pueda redimensionar
aplicacion.resizable(0, 0)

# Titulo de la ventana
aplicacion.title("Mi Reataurante - Sistema de Facturación")
# Color de fondo de la ventana
aplicacion.config(bg="lightblue", bd=1, relief=FLAT, padx=5, pady=5)

# ========== Panel superior ==========
panerl_superior = Frame(aplicacion, bd=1, relief=FLAT)
panerl_superior.pack(side=TOP)

etiqueta_titulo = Label(panerl_superior, text="Sistema de Facturación", fg="white", 
                       font=("Arial", 20), bg="azure4", width=35)
etiqueta_titulo.grid(row=0, column=0, padx=5, pady=5)

# ========== Panel Izquierdo ==========
panel_izquierdo = Frame(aplicacion, bd=1, bg="azure4", relief=FLAT, padx=5, pady=5)
panel_izquierdo.pack(side=LEFT)

# Panel Totales
panel_costos = Frame(panel_izquierdo, bd=1, bg="azure4", relief=FLAT, padx=5, pady=5)
panel_costos.pack(side=BOTTOM)

# Panel Comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comidas", 
                           bg="lightgrey", font=("Arial", 18, "bold"),
                           bd=1, relief=FLAT, padx=5, pady=5)
panel_comidas.pack(side=LEFT)

# Panel Bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", 
                           bg="lightgrey", font=("Arial", 18, "bold"),
                           bd=1, relief=FLAT, padx=5, pady=5)
panel_bebidas.pack(side=LEFT)

# Panel Postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", 
                           bg="lightgrey", font=("Arial", 18, "bold"),
                           bd=1, relief=FLAT, padx=5, pady=5)
panel_postres.pack(side=LEFT)

# Checkbuttons y cuadros de entrada
check_button_comidas(panel_comidas)
check_button_bebidas(panel_bebidas)
check_button_postres(panel_postres)

# RESUMEN DE PRECIOS
total_comidas = StringVar()
total_bebidas = StringVar()
total_postres = StringVar()
subtotal = StringVar()
impuestos = StringVar()
total = StringVar()

etiqueta_costo_comida = Label(panel_costos, text="Total Comidas", font=("Arial", 12, "bold"),
                            bg="azure4", fg="white")
texto_costo_comida = Entry(panel_costos, font=("Arial", 12, "bold"),
                        bd=1, width=10, state="readonly",
                        textvariable=total_comidas)
etiqueta_costo_bebida = Label(panel_costos, text="Total Bebidas", font=("Arial", 12, "bold"),
                            bg="azure4", fg="white")
texto_costo_bebida = Entry(panel_costos, font=("Arial", 12, "bold"),
                        bd=1, width=10, state="readonly",
                        textvariable=total_bebidas)
etiqueta_costo_postre = Label(panel_costos, text="Total Postres", font=("Arial", 12, "bold"),
                            bg="azure4", fg="white")
texto_costo_postre = Entry(panel_costos, font=("Arial", 12, "bold"),
                        bd=1, width=10, state="readonly",
                        textvariable=total_postres)

etiqueta_subtotal = Label(panel_costos, text="Subtotal", font=("Arial", 12, "bold"),
                            bg="azure4", fg="white")
texto_subtotal = Entry(panel_costos, font=("Arial", 12, "bold"),
                        bd=1, width=10, state="readonly",
                        textvariable=subtotal)
etiqueta_impuestos = Label(panel_costos, text="Impuestos", font=("Arial", 12, "bold"),
                            bg="azure4", fg="white")
texto_impuestos = Entry(panel_costos, font=("Arial", 12, "bold"),
                        bd=1, width=10, state="readonly",
                        textvariable=impuestos)
etiqueta_total = Label(panel_costos, text="Total", font=("Arial", 12, "bold"),
                            bg="azure4", fg="white")

texto_total = Entry(panel_costos, font=("Arial", 12, "bold"),
                        bd=1, width=10, state="readonly",
                        textvariable=total)

etiqueta_costo_comida.grid(row=0, column=0, padx=5, pady=5)
texto_costo_comida.grid(row=0, column=1, padx=5, pady=5)
etiqueta_costo_bebida.grid(row=1, column=0, padx=5, pady=5)
texto_costo_bebida.grid(row=1, column=1, padx=5, pady=5)
etiqueta_costo_postre.grid(row=2, column=0, padx=5, pady=5)
texto_costo_postre.grid(row=2, column=1, padx=5, pady=5)

etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal.grid(row=0, column=3, padx=5, pady=5)
etiqueta_impuestos.grid(row=1, column=2)
texto_impuestos.grid(row=1, column=3, padx=5, pady=5)
etiqueta_total.grid(row=2, column=2)
texto_total.grid(row=2, column=3, padx=10, pady=5)

# ========== Panel Derecho ==========
panel_derecho = Frame(aplicacion, bd=1, bg="azure4", relief=FLAT, padx=5, pady=5)
panel_derecho.pack(side=RIGHT)

# Panel Calculadora
panel_calculadora = Frame(panel_derecho, bd=1, bg="lightgrey", relief=FLAT)
panel_calculadora.pack()

generar_calculadora(panel_calculadora)

# Panel Recibo
panel_recibo = Frame(panel_derecho, bd=1, bg="lightgrey", relief=FLAT)
panel_recibo.pack()

generar_recibo(panel_recibo)

# Panel Botones
botones = ['total', 'recibo', 'guardar', 'resetear']
columnas = 0

def calcular_totales():   
    subtotal_comidas = 0
    indice_precios_comidas = 0
    for cantidad in texto_comidas:
        subtotal_comidas += float(cantidad.get()) * precios_comidas[indice_precios_comidas]
        indice_precios_comidas += 1
    
    subtotal_bebidas = 0
    indice_precios_bebidas = 0
    for cantidad in texto_bebidas:
        subtotal_bebidas += float(cantidad.get()) * precios_bebidas[indice_precios_bebidas]
        indice_precios_bebidas += 1
    
    subtotal_postres = 0
    indice_precios_postres = 0
    for cantidad in texto_postres:
        subtotal_postres += float(cantidad.get()) * precios_postres[indice_precios_postres]
        indice_precios_postres += 1
    
    calculo_subtotal = subtotal_comidas + subtotal_bebidas + subtotal_postres
    calculo_impuestos = calculo_subtotal * 0.21
    calculo_total = calculo_subtotal + calculo_impuestos
    
    total_comidas.set(f"{round(subtotal_comidas, 2)}€")
    total_bebidas.set(f"{round(subtotal_bebidas, 2)}€")
    total_postres.set(f"{round(subtotal_postres, 2)}€")
    
    subtotal.set(f"{round(calculo_subtotal, 2)}€")
    impuestos.set(f"{round(calculo_impuestos, 2)}€")
    total.set(f"{round(calculo_total, 2)}€")


panel_botones = Frame(panel_derecho, bd=1, bg="lightgrey", relief=FLAT)
panel_botones.pack()

for boton in botones:
    boton = Button(panel_botones, text=boton.title().capitalize(), font=("Arial", 14, "bold"),
                fg="white", bg="azure4", bd=1, width=10)
    boton.grid(row=0, column=columnas, padx=5, pady=5)
    columnas += 1
    
    if boton["text"] == "Total":
        boton.config(command=calcular_totales)



# Evitar que se cierre automáticamente
aplicacion.mainloop()