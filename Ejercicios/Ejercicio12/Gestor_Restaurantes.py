from tkinter import *

from comidas import check_button_comidas
from bebidas import check_button_bebidas
from postres import check_button_postres
from precios import generar_panel_totales, generar_panel_calculadora
from precios import calcular_totales, generar_recibo, guardar_recibo, resetear

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

generar_panel_totales(panel_costos, total_comidas, total_bebidas, total_postres, subtotal, impuestos, total)

# ========== Panel Derecho ==========
panel_derecho = Frame(aplicacion, bd=1, bg="azure4", relief=FLAT, padx=5, pady=5)
panel_derecho.pack(side=RIGHT)

# Panel Calculadora
panel_calculadora = Frame(panel_derecho, bd=1, bg="lightgrey", relief=FLAT)
panel_calculadora.pack()

generar_panel_calculadora(panel_calculadora)

# Panel Recibo
panel_recibo = Frame(panel_derecho, bd=1, bg="lightgrey", relief=FLAT)
panel_recibo.pack()

texto_recibo = Text(panel_recibo, font=("Arial", 12), bd=1, width=60, height=10)
texto_recibo.grid(row=0, column=0, padx=5, pady=5)

# Panel Botones
botones = ['total', 'recibo', 'guardar', 'resetear']
columnas = 0

panel_botones = Frame(panel_derecho, bd=1, bg="lightgrey", relief=FLAT)
panel_botones.pack()

for boton in botones:
    boton = Button(panel_botones, text=boton.title().capitalize(), font=("Arial", 14, "bold"),
                fg="white", bg="azure4", bd=1, width=10)
    boton.grid(row=0, column=columnas, padx=5, pady=5)
    columnas += 1
    
    if boton["text"] == "Total":
        boton.config(command=lambda: calcular_totales(total_comidas, total_bebidas, total_postres, subtotal, impuestos, total))
    elif boton["text"] == "Recibo":
        boton.config(command=lambda: generar_recibo(texto_recibo, total_comidas, total_bebidas, total_postres, subtotal, impuestos, total))
    elif boton["text"] == "Guardar":
        boton.config(command=lambda: guardar_recibo(texto_recibo))
    else:
        boton.config(command=lambda: resetear(texto_recibo, total_comidas, total_bebidas, total_postres, subtotal, impuestos, total))



# Evitar que se cierre automáticamente
aplicacion.mainloop()