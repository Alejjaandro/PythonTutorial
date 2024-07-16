import os
from pathlib import Path

# Obtener el directorio de trabajo
recetario = Path(__file__).resolve().parent / "Recetas"

# MENU
def menu():
    # Limpiar terminal
    os.system("cls")
    
    # Obtener numero de recetas
    recetas = 0
    for directory in os.listdir(recetario):
        for file in os.listdir(recetario / directory):
            recetas += 1
    
    print("-"*50)
    print("\nHola!, bienvenido al recetario de cocina \n")
    print("Se encuentra en el directorio: ", recetario)
    print(f"Tienes: {recetas} recetas \n")

    opciones = ["1. Leer receta", "2. Crear receta", "3. Crear categoría", "4. Eliminar receta", "5. Eliminar categoría", "6. Finalizar Programa"]
    for opcion in opciones:
        print(opcion)
    
    print("\nQue desea hacer?")
    
menu()
opcion = input("\nIngrese la opción que desea realizar: ")


# OPERACIONES

def mostrar_categorias():
    indice = 1
    lista_categorias = []
    
    print("\nCategorias disponibles: \n")
    for directory in os.listdir(recetario):
        print(f" [{indice}] {directory}")
        lista_categorias.append(directory)
        indice += 1
    
    return lista_categorias
        
def mostrar_recetas(categoria):
    indice = 1
    lista_recetas = []
    
    print("\nRecetas disponibles: \n")
    for receta in os.listdir(recetario / categoria):
        print(f" [{indice}] {receta}")
        lista_recetas.append(receta)
        indice += 1
    
    return lista_recetas

def leer_receta():
    print("\nQue receta desea leer?")
    categorias = mostrar_categorias()
    indice_categorias = input("\nElija la categoria: ")
    categoria = categorias[int(indice_categorias) - 1]
    
    recetas = mostrar_recetas(categoria)
    indice_recetas = input("\nElija la receta: ")
    receta = recetas[int(indice_recetas) - 1]
    
    with open(recetario / categoria / receta, "r") as file:
        print(file.read())
        file.close()
        
def crear_receta():
    print("\nQue receta desea crear?")
    
    categorias = mostrar_categorias()
    indice_categorias = input("\nElija la categoria: ")
    categoria = categorias[int(indice_categorias) - 1]
    
    receta = input("Ingrese el nombre de la receta: ")
    preparacion = input("Ingrese la receta: ")
    
    with open(recetario / categoria / (f"{receta}.txt"), "w") as file:
        file.write(preparacion)
        file.close()
        
    print("\nReceta creada con éxito!")
    
def crear_categoria():
    print("\nQue categoria desea crear?")
    
    categoria = input("Ingrese el nombre de la categoria: ")
    
    os.mkdir(recetario / categoria)
    print("\nCategoria creada con éxito!")

def eliminar_receta():
    print("\nQue receta desea eliminar?")
    
    categorias = mostrar_categorias()
    indice_categorias = input("\nElija la categoria: ")
    categoria = categorias[int(indice_categorias) - 1]
    
    recetas = mostrar_recetas(categoria)
    indice_recetas = input("\nElija la receta: ")
    receta = recetas[int(indice_recetas) - 1]
    
    os.remove(recetario / categoria / receta)
    print("\nReceta eliminada con éxito!")

def eliminar_categoria():
    print("\nQue categoria desea eliminar?")
    
    categorias = mostrar_categorias()
    indice_categorias = input("\nElija la categoria: ")
    categoria = categorias[int(indice_categorias) - 1]
    
    os.rmdir(recetario / categoria)
    print("\nCategoria eliminada con éxito!")

while opcion != "6":
    
    if opcion == "1":
        leer_receta()
        input("\nPresione Enter para continuar...")
        pass
    
    elif opcion == "2":
        crear_receta()
        input("\nPresione Enter para continuar...")    
        pass
    
    elif opcion == "3":
        crear_categoria()
        input("\nPresione Enter para continuar...")
      
        pass
    
    elif opcion == "4":
        eliminar_receta()
        input("\nPresione Enter para continuar...")     
        pass
    
    elif opcion == "5":
        eliminar_categoria()
        input("\nPresione Enter para continuar...")
        pass
    
    else:
        print("Opción no válida, intente de nuevo")

    menu()
    opcion = input("\nIngrese la opción que desea realizar: ")
    
else:
    print("Programa finalizado")
    os.system("cls")