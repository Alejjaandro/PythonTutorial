from tkinter import *
from tkinter import filedialog, messagebox
from random import randint
import datetime

from comidas import lista_de_comidas, texto_comidas, precios_comidas, cuadros_comidas, variables_comidas
from bebidas import lista_de_bebidas, texto_bebidas, precios_bebidas, cuadros_bebidas, variables_bebidas
from postres import lista_de_postres, texto_postres, precios_postres, cuadros_postres, variables_postres

# ========== Calculadora ==========
operador = ""
def click_boton(valor, visor):
    global operador
    operador = operador + valor
    visor.delete(0, END)
    visor.insert(END, operador)

def borrar(visor):
    global operador
    operador = ""
    visor.delete(0, END)
    
def calcular(visor):
    global operador
    try:
        resultado = str(eval(operador))
        visor.delete(0, END)
        visor.insert(0, resultado)
        operador = ""
    except:
        visor.delete(0, END)
        visor.insert(0, "Error")

def generar_panel_calculadora(panel_calculadora):
    
    visor = Entry(panel_calculadora, font=("Arial", 16, "bold"), bd=1, width=45)
    visor.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
    
    botones_calculadora = [
        "7", "8", "9", "+",
        "4", "5", "6", "-",
        "1", "2", "3", "*",
        "=", "0", "Borrar", "/"
    ]
    fila = 1
    columna = 0
    
    for boton in botones_calculadora:
        boton = Button(panel_calculadora, text=boton.title(), font=("Arial", 14, "bold"),
                    fg="white", bg="azure4", bd=1, width=5)
        boton.grid(row=fila, column=columna, padx=5, pady=5)
        
        # Ajustar posición de los botones
        if columna == 3:
            fila += 1   
                       
        columna += 1
         
        if columna == 4:
            columna = 0
            
        # Asignar funcionalidad a los botones
        if boton["text"] != "=" and boton["text"] != "Borrar":
            boton.config(command=lambda boton=boton: click_boton(boton["text"], visor))
        elif boton["text"] == "Borrar":
            boton.config(command=lambda boton=boton: borrar(visor))
        else:
            boton.config(command=lambda boton=boton: calcular(visor))

# ========= Totales =========
def generar_panel_totales(panel_costos, total_comidas, total_bebidas, total_postres, subtotal, impuestos, total):
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

def calcular_totales(total_comidas, total_bebidas, total_postres, subtotal, impuestos, total):
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

# ========= Recibo ========== 
def generar_recibo(texto_recibo, total_comidas, total_bebidas, total_postres, subtotal, impuestos, total):
    texto_recibo.delete(1.0, END)
    num_recibo = f"N# - {randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    
    texto_recibo.insert(END, f'Fra. {num_recibo}\t\t{fecha}\n')
    texto_recibo.insert(END, f'*' * 60 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 60 + '\n')
    
    x = 0
    for comida in texto_comidas:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_de_comidas[x]}\t\t{comida.get()}\t'
                                     f'{int(comida.get()) * precios_comidas[x]}€\n')
        x += 1

    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_de_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'{int(bebida.get()) * precios_bebidas[x]}€\n')
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_de_postres[x]}\t\t{postres.get()}\t'
                                     f'{int(postres.get()) * precios_postres[x]}€\n')
        x += 1

    texto_recibo.insert(END, f'-' * 60 + '\n')
    texto_recibo.insert(END, f' Costo de la Comida: \t\t\t{total_comidas.get()}\n')
    texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{total_bebidas.get()}\n')
    texto_recibo.insert(END, f' Costo de la Postres: \t\t\t{total_postres.get()}\n')
    texto_recibo.insert(END, f'-' * 60 + '\n')
    texto_recibo.insert(END, f' Sub-total: \t\t\t{subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t\t{impuestos.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{total.get()}\n')
    texto_recibo.insert(END, f'*' * 60 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto!')

 # ========== Calcular Totales ==========

def guardar_recibo(texto_recibo):
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", title="Guardar Recibo", defaultextension=".txt")
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Recibo Guardado", "El recibo ha sido guardado con éxito!")

# ========== Resetear ==========
def resetear(texto_recibo, total_comidas, total_bebidas, total_postres, subtotal, impuestos, total):
    texto_recibo.delete(0.1, END)

    for texto in texto_comidas:
        texto.set('0')
    for texto in texto_bebidas:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comidas:
        v.set(0)
    for v in variables_bebidas:
        v.set(0)
    for v in variables_postres:
        v.set(0)

    total_comidas.set('')
    total_bebidas.set('')
    total_postres.set('')
    subtotal.set('')
    impuestos.set('')
    total.set('')