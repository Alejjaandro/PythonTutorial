from tkinter import *

# ========== Calculadora ==========
# Funcionalidades    
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

def generar_calculadora(panel_calculadora):
    
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
    
# ========= Recibo ==========
def generar_recibo(panel_recibo):
    texto_recibo = Text(panel_recibo, font=("Arial", 12), bd=1, width=60, height=10)
    texto_recibo.grid(row=0, column=0, padx=5, pady=5)
