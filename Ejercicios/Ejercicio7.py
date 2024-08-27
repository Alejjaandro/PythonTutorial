from random import randint
import os

class Persona:
    def __init__(self, nombre, apeellido):
        self.nombre = nombre
        self.apellido = apeellido
        
class Cliente(Persona):
    numero_cuenta = f"{randint(1000, 9999)}-{randint(1000, 9999)}-{randint(1000, 9999)}-{randint(1000, 9999)}"
    balance = 0
        
    def __str__(self):
        return(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nNumero de cuenta: {self.numero_cuenta}\nBalance: {self.balance}€")
    
    def deposito(self, cantidad):
        self.balance += cantidad
        return self.balance
    
    def retirar(self, cantidad):
        if cantidad > self.balance:
            return "Fondos insuficientes"
        else:
            self.balance -= cantidad
            return self.balance 

opciones = {1: "Consultar perfil", 2: "Depositar", 3: "Retirar", 4: "Salir"}

def inicio_sesion():
    os.system("cls")
    print("=" * 20)
    print("Inicio de sesion")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    print("=" * 20)
    return Cliente(nombre, apellido)

def menu(nombre, apellido):
    print(f"\nBienvenido {nombre} {apellido}, que desea hacer?\n")
    
    for key, value in opciones.items():
        print(f"{key}. {value}")
        

def main():
    cliente = inicio_sesion()
    
    menu(cliente.nombre, cliente.apellido)
    opcion = int(input("Opcion: "))
    
    while opcion != 4:          
        if opcion == 1:
            print("\nPerfil del cliente:")
            print(cliente)
        elif opcion == 2:
            cantidad = int(input("Cantidad a depositar: "))
            print(f"\nBalance actual: {cliente.deposito(cantidad)}€")
        elif opcion == 3:
            cantidad = int(input("Cantidad a retirar: "))
            print(f"\nBalance actual: {cliente.retirar(cantidad)}€")
        elif opcion == 4:
            break
        else:
            print("Opcion invalida")
        
        input("\nPresione enter para continuar...")
        os.system("cls")
        
        menu(cliente.nombre, cliente.apellido)
        opcion = int(input("Opcion: "))
        
    print("\nGracias por usar nuestros servicios!")

main()