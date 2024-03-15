import pygame
import math


pygame.init()

ancho_pantalla = 800
alto_pantalla = 600
ventana = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
color_pantalla = (255, 255, 255)
color_dibujo = (0, 0, 0)
ventana.fill(color_pantalla)


radio_circulo = 20
ruta = []
dibujando_ruta = False
moviendo_circulo = False
circulo_pos = (ancho_pantalla // 2, alto_pantalla // 2)  

def dibujar_circulo(ventana, centro, radio):
    if centro:  
        pygame.draw.circle(ventana, color_dibujo, centro, radio, 1)


ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if not moviendo_circulo:  # Comenzar nueva ruta si no se está moviendo el círculo
                ruta = [evento.pos]
                dibujando_ruta = True
        elif evento.type == pygame.MOUSEMOTION and dibujando_ruta:
            ruta.append(evento.pos)
        elif evento.type == pygame.MOUSEBUTTONUP and dibujando_ruta:
            dibujando_ruta = False
            moviendo_circulo = True
            circulo_pos = ruta[0]

    if not moviendo_circulo:
        ventana.fill(color_pantalla)
        if len(ruta) > 1:
            pygame.draw.lines(ventana, color_dibujo, False, ruta, 1)
        dibujar_circulo(ventana, circulo_pos, radio_circulo)
        pygame.display.flip()

    if moviendo_circulo:
        if ruta:
            siguiente_punto = ruta.pop(0)
            ventana.fill(color_pantalla)
            if len(ruta) > 1:
                pygame.draw.lines(ventana, color_dibujo, False, ruta, 1)
            dibujar_circulo(ventana, siguiente_punto, radio_circulo)
            pygame.display.flip()
            pygame.time.delay(50)
        else:
            moviendo_circulo = False
            if len(ruta) > 0:
                circulo_pos = ruta[-1]

pygame.quit()
