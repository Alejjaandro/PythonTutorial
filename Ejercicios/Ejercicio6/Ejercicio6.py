import os
from pathlib import Path

# C:\Users\Alejandro\Documents\-- PROGRAMACION --\Python\Ejercicios\Ejercicio6

# Obtener el directorio de trabajo
recetario = Path(__file__).resolve().parent / "Recetas"

# Limpiar terminal
os.system("cls")

# Obtener numero de recetas
recetas = 0
for directory in os.listdir(recetario):
    for file in os.listdir(recetario / directory):
        recetas += 1

# MENU
def menu():
    opciones = ["1. Leer receta", "2. Crear receta", "3. Crear categoría", "4. Eliminar receta", "5. Eliminar categoría", "6. Finalizar Programa"]
    for opcion in opciones:
        print(opcion)
    
    print("\nQue desea hacer? \n")
    
print("\nHola!, bienvenido al recetario de cocina \n")
print("Se encuentra en el directorio: ", recetario)
print(f"Tienes: {recetas} recetas \n")

menu()
opcion = input("\nIngrese la opción que desea realizar: ")


# OPERACIONES
while opcion != "6":
    
    if opcion == "1":
        print("\nQue receta desea leer?")
        categoria = input("Elija la categoria: ")
        print("\nRecetas disponibles: ")
        for receta in os.listdir(recetario / categoria):
            print(receta)
            
        receta = input("\nElija la receta: ")
        with open(recetario / categoria / receta, "r") as file:
            print(file.read())
            file.close()
        pass
    
    elif opcion == "2":
        print("\nQue receta desea crear?")
        categoria = input("Elija la categoria: ")
        receta = input("Elija el nombre de la receta: ")
        preparacion = input("Ingrese la receta: ")
        with open(recetario / categoria / (f"{receta}.txt"), "w") as file:
            file.write(preparacion)
            file.close()
        
        print("\nReceta creada con éxito!")
        
        pass
    
    elif opcion == "3":
        print("\nQue categoria desea crear?")
        categoria = input("Elija el nombre de la categoria: ")
        os.mkdir(recetario / categoria)
        print("\nCategoria creada con éxito!")
        
        pass
    
    elif opcion == "4":
        print("\nQue receta desea eliminar?")
        categoria = input("Elija la categoria: ")
        print("\nRecetas disponibles: ")
        for receta in os.listdir(recetario / categoria):
            print(receta)
        receta = input("\nElija la receta: ")
        os.remove(recetario / categoria / receta)
        print("\nReceta eliminada con éxito!")
        
        pass
    
    elif opcion == "5":
        print("\nQue categoria desea eliminar?")
        for categoria in os.listdir(recetario):
            print(categoria)
        categoria = input("\nElija la categoria: ")
        os.rmdir(recetario / categoria)
        print("\nCategoria eliminada con éxito!")
        
        pass
    
    else:
        print("Opción no válida, intente de nuevo")

    print("================================")
    menu()
    opcion = input("Ingrese la opción que desea realizar: ")
    
else:
    print("Programa finalizado")
