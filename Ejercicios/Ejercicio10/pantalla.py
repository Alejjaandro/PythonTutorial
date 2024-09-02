import pygame

# Creamos una ventana de 800x600
pantalla = pygame.display.set_mode([800,600])

# Titulo de la ventana
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("extraterrestre.png")
pygame.display.set_icon(icono)
