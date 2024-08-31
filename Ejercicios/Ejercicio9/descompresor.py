import shutil
from pathlib import Path

ruta = Path("Python/Ejercicios/Ejercicio9/Proyecto_Dia_9.zip")
print(ruta)

shutil.unpack_archive(ruta, "Python/Ejercicios/Ejercicio9", "zip")
