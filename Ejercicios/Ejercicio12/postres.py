from tkinter import *

lista_de_postres = ["Arroz con leche", "Mazamorra morada", "Mazamorra de calabaza", "Turrón de Doña Pepa", "Picarones", "Suspiro a la limeña", "Alfajores", "Besos de moza", "King Kong", "Queso helado"]
precios_postres = [5, 4, 4, 3, 3, 4, 2, 2, 2, 3]
contador_postres = 0
variables_postres = []
cuadros_postres = []
texto_postres = []

def revisar_estado_postres():
    x = 0
    for postre in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == "0":
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set(0)
        x += 1        

def check_button_postres(panel_postres):
    global contador_postres, variables_postres, cuadros_postres, texto_postres
    
    for postre in lista_de_postres:
        # Crear Checkbutton
        variables_postres.append('')
        variables_postres[contador_postres] = IntVar()

        postre = Checkbutton(panel_postres, text=postre.title(), bg="lightgrey", font=("Arial", 14, "bold"),
                            onvalue=1, offvalue=0, 
                            variable=variables_postres[contador_postres],
                            command=revisar_estado_postres)
        postre.grid(row=contador_postres, column=0, sticky=W)
        
        # Crear cuadros de entrada
        cuadros_postres.append('')
        texto_postres.append('')
        texto_postres[contador_postres] = StringVar()
        texto_postres[contador_postres].set(0)

        cuadros_postres[contador_postres] = Entry(panel_postres, font=("Arial", 14, "bold"), 
                                                bd=1, width=5, state=DISABLED,
                                                textvariable=texto_postres[contador_postres])
        cuadros_postres[contador_postres].grid(row=contador_postres, column=1)

        contador_postres += 1