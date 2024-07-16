nombre = input("Cual es tu nombre?: ")
ventas = input("Cuanto vendiste?: ")
print(f"Ok, {nombre}, este mes ganaste: {float(ventas) * 0.13}€")

# Otra forma de hacerlo
""" 
nombre = input("Cual es tu nombre?: ")
ventas = input("Cuanto vendiste?: ")

ventas = float(ventas)
comision = ventas * 0.13
comision = round(comision, 2)

print(f"Ok, {nombre}, este mes ganaste: {comision}€")
 """