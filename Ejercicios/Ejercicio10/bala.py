import pygame
import math
from pantalla import pantalla

# ----- Bala ------   
# Variables de la bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_y_cambio = 20
bala_disparada = False

# Funcion para dibujar la bala
def disparar_bala(x, y):
    # global bala_disparada
    # bala_disparada = True
    # print("Disparar bala")
    # Dibujamos la bala en la posicion del jugador + 16 pixeles
    pantalla.blit(img_bala, (x + 16, y + 10))


# Funcion para detectar colisiones
def colision(x1, y1, x2, y2):
    # Calculamos la distancia entre dos puntos: d = sqrt((x2-x1)^2 + (y2-y1)^2)
    operacion1 = math.pow(x2 - x1, 2)
    operacion2 = math.pow(y2 - y1, 2)
    distancia = math.sqrt(operacion1 + operacion2)
    if distancia < 27:
        return True
    else:
        return False
