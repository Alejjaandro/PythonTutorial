import random

nombre = input("Ingrese su nombre: ")
num_aleatorio = random.randint(1, 101)

print(f"Hola, {nombre}, estoy pensando en un número entre 1 y 100. Adivina cuál es. Tienes 8 intentos.")

intentos = 0

while intentos < 8:
    num_usuario = int(input("\nIngrese un número: "))
    intentos += 1
    
    if num_usuario not in range(1, 101):
        print("El número debe estar entre 1 y 100.")
    elif num_usuario > num_aleatorio:
        print(f"El número es menor. Le quedan {8 - intentos} intentos.")
    elif num_usuario < num_aleatorio:
        print(f"El número es mayor. Le quedan {8 - intentos} intentos.")
    else:
        print(f"\nFelicidades, {nombre}, has adivinado el número en {intentos} intentos.")
        break
else:
    print(f"\nLo siento, {nombre}, has agotado tus 8 intentos. El número era {num_aleatorio}.")