from tkinter import *

lista_de_bebidas = ["Inca Kola", "Coca Cola", "Pepsi", "Sprite", "Fanta", "Agua", "Chicha morada", "Chicha de jora", "Cerveza", "Vino"]
precios_bebidas = [1.5, 2, 2, 2, 2, 1, 1.5, 1.5, 2.5, 3]
contador_bebidas = 0
variables_bebidas = []
cuadros_bebidas = []
texto_bebidas = []

def revisar_estado_bebidas():
    x = 0
    for bebida in cuadros_bebidas:
        if variables_bebidas[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == "0":
                cuadros_bebidas[x].delete(0, END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set(0)
        x += 1        

def check_button_bebidas(panel_bebidas):
    global contador_bebidas, variables_bebidas, cuadros_bebidas, texto_bebidas
    
    for bebida in lista_de_bebidas:
        # Crear Checkbutton
        variables_bebidas.append('')
        variables_bebidas[contador_bebidas] = IntVar()
        
        bebida = Checkbutton(panel_bebidas, text=bebida.title(), bg="lightgrey", font=("Arial", 14, "bold"),
                            onvalue=1, offvalue=0, 
                            variable=variables_bebidas[contador_bebidas],
                            command=revisar_estado_bebidas)
        bebida.grid(row=contador_bebidas, column=0, sticky=W)
        
        # Crear cuadros de entrada
        cuadros_bebidas.append('')
        texto_bebidas.append('')
        texto_bebidas[contador_bebidas] = StringVar()
        texto_bebidas[contador_bebidas].set(0)

        cuadros_bebidas[contador_bebidas] = Entry(panel_bebidas, font=("Arial", 14, "bold"), 
                                                bd=1, width=5, state=DISABLED,
                                                textvariable=texto_bebidas[contador_bebidas])
        cuadros_bebidas[contador_bebidas].grid(row=contador_bebidas, column=1)

        contador_bebidas += 1