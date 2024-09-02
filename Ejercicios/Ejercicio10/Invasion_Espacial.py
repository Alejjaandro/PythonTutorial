import pygame
import random
import math
from pygame import mixer
import io

# Inicializamos pygame
pygame.init()

# Creamos una ventana de 800x600
pantalla = pygame.display.set_mode([800,600])

# Titulo de la ventana
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("extraterrestre.png")
pygame.display.set_icon(icono)

# ----- Informacion del juego ------
# Fuente a bytes
def fuente_bytes(nombre_fuente):
    with open(nombre_fuente, "rb") as archivo:
        tff_bytes = archivo.read()
    return io.BytesIO(tff_bytes)

fuente_como_bytes = fuente_bytes("Alontela-Black.otf")

# Puntuación
puntos = 0
fuente = pygame.font.Font(fuente_como_bytes, 36)
texto_x = 10
texto_y = 10

def mostrar_puntos(x, y):
    texto = fuente.render(f"Puntos: {puntos}", True, (255,255,255))
    pantalla.blit(texto, (x, y))
    
# Musica de fondo
mixer.music.load("MusicaFondo.mp3")
mixer.music.play(-1)

# Texto final
fuente_final = pygame.font.Font(fuente_como_bytes, 64)
def texto_final():
    texto = fuente_final.render("GAME OVER", True, (255,255,255))
    pantalla.blit(texto, (200, 250))

# ----- Jugador ------
# Variables del Jugador
img_jugador = pygame.image.load("nave_espacial.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Funcion para dibujar al jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

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

# ----- Bala ------   
# Variables de la bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_y_cambio = 20
bala_disparada = False

# Funcion para dibujar la bala
def disparar_bala(x,y):
    global bala_disparada
    bala_disparada = True
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




# ===== Bucle principal =====
se_ejecuta = True
while se_ejecuta:
    # pantalla.fill((0,0,150))
    pantalla.blit(pygame.image.load("fondo_espacio.png"), (0,0))
    
    # Eventos
    for evento in pygame.event.get():
        # Si se presiona el boton de cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        # Si se presiona una tecla
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio -= 5
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio += 5
            if evento.key == pygame.K_SPACE and not bala_disparada:
                mixer.Sound("disparo.mp3").play()
                bala_x = jugador_x
                disparar_bala(bala_x, bala_y)
                
        # Si se suelta una tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
                
    # Actualizamos la posicion del jugador
    jugador_x += jugador_x_cambio
    
    # Limitamos el movimiento del jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
        
    # Actualizamos la posicion del enemigo
    for i in range(cantidad_enemigos):
        # Fin del juego
        if enemigo_y[i] > 450:
            for j in range(cantidad_enemigos):
                enemigo_y[j] = 2000
            texto_final()
            break
        
        enemigo_x[i] += enemigo_x_cambio[i]
    
        # Limitamos el movimiento del  enemigo
        if enemigo_x[i] <= 0:
            enemigo_x_cambio[i] = enemigo_x_cambio[i] * -1
            enemigo_y[i] += enemigo_y_cambio[i]
        elif enemigo_x[i] >= 736:
            enemigo_x_cambio[i] = -enemigo_x_cambio[i]
            enemigo_y[i] += enemigo_y_cambio[i]
        
        # Detectamos colisiones
        hay_colision = colision(enemigo_x[i], enemigo_y[i], bala_x, bala_y)
        if hay_colision:
            mixer.Sound("Golpe.mp3").play()
            bala_y = 500
            bala_disparada = False
            puntos += 1
            enemigo_x[i] = random.randint(0, 736)
            enemigo_y[i] = random.randint(50, 200) 

        # Dibujamos al enemigo
        enemigo(enemigo_x[i], enemigo_y[i])

        
    # Actualizamos la posicion de la bala
    if bala_disparada:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio
    
    # Limitamos el movimiento de la bala
    if bala_y <= 0:
        bala_y = 500
        bala_disparada = False
        
    # Mostramos la puntuacion
    mostrar_puntos(texto_x, texto_y)
        
    # Dibujamos al jugador 
    jugador(jugador_x, jugador_y)
        
    # Actualizamos la pantalla
    pygame.display.update()  
