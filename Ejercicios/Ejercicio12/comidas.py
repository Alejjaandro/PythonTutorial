from tkinter import *

lista_de_comidas = ["Pollo a la brasa", "Lomo saltado", "Ceviche", "Arroz con pollo", "Seco de cordero", "Aji de gallina", "Causa rellena", "Papa a la huancaína", "Rocoto relleno", "Anticuchos"]
precios_comidas = [20, 25, 30, 15, 35, 18, 12, 10, 8, 5]
contador_comidas = 0
variables_comidas = []
cuadros_comidas = []
texto_comidas = []

def revisar_estado_comidas():
    x = 0
    for comida in cuadros_comidas:
        if variables_comidas[x].get() == 1:
            cuadros_comidas[x].config(state=NORMAL)
            if cuadros_comidas[x].get() == "0":
                cuadros_comidas[x].delete(0, END)
            cuadros_comidas[x].focus()
        else:
            cuadros_comidas[x].config(state=DISABLED)
            texto_comidas[x].set(0)
        x += 1        
    
def check_button_comidas(panel_comidas):
    global contador_comidas, variables_comidas, cuadros_comidas, texto_comidas
    
    for comida in lista_de_comidas:
        # Crear Checkbutton
        variables_comidas.append('')
        variables_comidas[contador_comidas] = IntVar()
        
        comida = Checkbutton(panel_comidas, text=comida.title(), bg="lightgrey", font=("Arial", 14, "bold"),
                            onvalue=1, offvalue=0, 
                            variable=variables_comidas[contador_comidas],
                            command=revisar_estado_comidas)
        comida.grid(row=contador_comidas, column=0, sticky=W)
        
        # Crear cuadros de entrada
        cuadros_comidas.append('')
        texto_comidas.append('')
        texto_comidas[contador_comidas] = StringVar()
        texto_comidas[contador_comidas].set(0)
        
        cuadros_comidas[contador_comidas] = Entry(panel_comidas, font=("Arial", 14, "bold"), 
                                                bd=1, width=5, state=DISABLED,
                                                textvariable=texto_comidas[contador_comidas])
        cuadros_comidas[contador_comidas].grid(row=contador_comidas, column=1)
        
        contador_comidas += 1