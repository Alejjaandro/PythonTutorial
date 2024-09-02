import pygame
from pantalla import pantalla
import random

# ----- Enemigo ------
# Variables del Enemigo
img_enemigo = pygame.image.load("nave_alien.png")
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 5

for indice in range(cantidad_enemigos):
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(7.5)
    enemigo_y_cambio.append(50)

    # Funcion para dibujar al enemigo
    def enemigo(x, y):
        pantalla.blit(img_enemigo, (x, y))
