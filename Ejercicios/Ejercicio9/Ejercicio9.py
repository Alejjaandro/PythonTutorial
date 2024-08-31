import os
import re
import datetime
import time
from pathlib import Path

ruta = Path("Python/Ejercicios/Ejercicio9/Mi_Gran_Directorio")

patron = re.compile(r"N\D{3}-\d{5}")

fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def bucador_num_series(ruta, patron):
    os.system("cls")
    
    total_num = 0
    tiempo_inicio = time.time()
    
    print("----------------------------------------------------")
    print(f"Fecha de búsqueda: {fecha_actual}")
    print("\nARCHIVO\t\tNRO. SERIE")
    print("-------\t\t----------")
    
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            ruta_archivo = os.path.join(carpeta, arch)
            
            file = open(ruta_archivo, "r")
            contenido = file.read()
            
            if re.search(patron, contenido):
                total_num += 1
                print(f"{arch}\t{re.search(patron, contenido).group()}")
                
            file.close()
            
    tiempo_final = time.time() - tiempo_inicio
    print(f"\nNúmeros encontrados: {total_num}")
    print(f"Duración de la búsqueda: {round(tiempo_final, 3)} segundos")
    print("----------------------------------------------------")
    
bucador_num_series(ruta, patron)