def num_perfumeria():
    turno = 1
    while True:
        yield f"P - {turno}"
        turno += 1
        
def num_farmacia():
    turno = 1
    while True:
        yield f"F - {turno}"
        turno += 1

def  num_cosmeticos():
    turno = 1
    while True:
        yield f"C - {turno}"
        turno += 1


perfumeria = num_perfumeria()
farmacia = num_farmacia()
cosmeticos = num_cosmeticos()

def mostrar_turno(servicio):
    
    print("\n" + "*" * 23)
    print("Su turno es:")
                
    if servicio == "perfumeria":
        print(next(perfumeria))
    elif servicio == "farmacia":
        print(next(farmacia))
    elif servicio == "cosmeticos":
        print(next(cosmeticos))
    
    print("Gracias por su espera")
    print("*" * 23 + "\n")
