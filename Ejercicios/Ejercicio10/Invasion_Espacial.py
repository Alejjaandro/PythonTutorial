import pygame
import random
from pygame import mixer

from pantalla import pantalla
from jugador import jugador, jugador_x, jugador_y, jugador_x_cambio
from enemigos import cantidad_enemigos, enemigo, enemigo_x, enemigo_y, enemigo_x_cambio, enemigo_y_cambio
from bala import disparar_bala, colision, bala_disparada, bala_x, bala_y, bala_y_cambio
from info_juego import mostrar_puntos, texto_final

# Inicializamos pygame
pygame.init()

# ----- Informacion del juego ------
puntos = 0

# Musica de fondo
mixer.music.load("MusicaFondo.mp3")
mixer.music.play(-1)

# ===== Bucle principal =====
se_ejecuta = True
while se_ejecuta:
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
                bala_disparada = True
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
    mostrar_puntos(puntos)
        
    # Dibujamos al jugador 
    jugador(jugador_x, jugador_y)
        
    # Actualizamos la pantalla
    pygame.display.update()
