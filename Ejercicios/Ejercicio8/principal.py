from numeros import mostrar_turno
import os

salir = False

while not salir:
    
    print("Bienvenido!\n")
    print("1. Mostrar turno de farmacia")
    print("2. Mostrar turno de perfumería")
    print("3. Mostrar turno de cosméticos")
    print("4. Salir")
    
    try:
        
        opcion = int(input("\nIngrese una opción: "))
        
        if opcion == 1:
            mostrar_turno("farmacia")
            input("Presione Enter para continuar")
        elif opcion == 2:
            mostrar_turno("perfumeria")
            input("Presione Enter para continuar")
        elif opcion == 3:
            mostrar_turno("cosmeticos")
            input("Presione Enter para continuar")
        elif opcion == 4:
            salir = True
            
    except ValueError:
        print("\nOpción incorrecta".upper())
        input("\nPresione Enter para continuar")
    
    os.system("cls")

print("Gracias por utilizar nuestro servicio")