from random import choice
from os import system

palabras = ['python', 'java', 'javascript', 'html', 'css']

vidas = 6

palabra = choice(palabras)
palabra_oculta = ['_' for letra in palabra]
letras_incorrectas = set([])

def introducir_letra():    
    letra = input('\nIntroduce una letra: ')
    
    while len(letra) != 1 or not letra.isalpha():
        print('Esa letra no es válida.')
        print('\n')
        letra = input('Introduce una letra válida: ')
        
    return letra

def comprobar_letra(letra, palabra, palabra_oculta, vidas):
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_oculta[i] = letra
    else:
        vidas -= 1
        print(f'\nEsa letra no se encuentra en la palabra. \nTe quedan {vidas} vidas.')
        letras_incorrectas.add(letra)
        
    return vidas

while vidas > 0:
    print('\n' + '*' * 20 + '\n')
    
    print('Adivina la palabra:')
    print(' '.join(palabra_oculta))
    print('\n')
    print(f'Letras incorrectas: {", ".join(letras_incorrectas)}')
    print(f'Vidas: {vidas}')
    
    print('\n' + '*' * 20 + '\n')
        
    letra = introducir_letra()
    vidas = comprobar_letra(letra, palabra, palabra_oculta, vidas)
    
    system('cls')
    
    if palabra_oculta == list(palabra):
        print('\n¡Has ganado!')
        print(f'La palabra era "{palabra}"')
        break
else:
    print(f'¡Has perdido! La palabra era "{palabra}"')