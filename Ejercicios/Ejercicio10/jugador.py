# Variables del Jugador
import pygame
from pantalla import pantalla

img_jugador = pygame.image.load("nave_espacial.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Funcion para dibujar al jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))
