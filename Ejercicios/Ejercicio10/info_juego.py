import pygame
from pantalla import pantalla
import io

# Fuente a bytes
def fuente_bytes(nombre_fuente):
    with open(nombre_fuente, "rb") as archivo:
        tff_bytes = archivo.read()
    return io.BytesIO(tff_bytes)

fuente_como_bytes = fuente_bytes("Alontela-Black.otf")

# Puntuación
pygame.font.init()
fuente = pygame.font.Font(fuente_como_bytes, 32)
texto_x = 10
texto_y = 10

def mostrar_puntos(puntos):
    texto = fuente.render(f"Puntos: {puntos}", True, (255,255,255))
    pantalla.blit(texto, (texto_x, texto_y))
    
# Texto final
fuente_final = pygame.font.Font(fuente_como_bytes, 64)
def texto_final():
    texto = fuente_final.render("GAME OVER", True, (255,255,255))
    pantalla.blit(texto, (250, 250))
