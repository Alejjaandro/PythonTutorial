texto = input("Introduce un texto: ")
print("\n")

# Cuantas veces aparece cada letra en el texto
print("LETRAS EN EL TEXTO")
letras = [input("Introduce una letra: "), input("Introduce otra letra: "), input("Introduce otra letra: ")]
print(letras)
for letra in letras:
    letra = letra.lower()
    texto = texto.lower()
    print(f"La letra '{letra}' aparece {texto.count(letra)} veces en el texto")

# Cuantas palabras tiene el texto
num_palabras = texto.split()
print("\n")
print("NÚMERO DE PALABRAS")
print(f"El texto tiene {len(num_palabras)} palabras")

# Primera y última letra del texto
primera_letra = texto[0]
ultima_letra = texto[-1]
print("\n")
print("PRIMERA Y ÚLTIMA LETRA DEL TEXTO")
print(f"La primera letra del texto es {primera_letra} y la última letra es {ultima_letra}")

# Texto invertido
palabras_invertidas = texto.split()[::-1]
print("\n")
print("TEXTO INVERTIDO")
print("El texto invertido es:")
print(" ".join(palabras_invertidas))

# Si la palabra "Python" está en el texto
python = {True: "La palabra 'Python' está en el texto", False: "La palabra 'Python' no está en el texto"}
print("\n")
print("PALABRA PYTHON")
print(python["python" in texto.lower()])