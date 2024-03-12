import pygame

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
ancho_pantalla = 800
alto_pantalla = 600
ventana = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
color_pantalla = (255, 255, 255)
color_dibujo = (0, 0, 0)

# Inicializa la pantalla con el color de fondo
ventana.fill(color_pantalla)

# Variables para el círculo y la ruta
circulo_pos = (ancho_pantalla // 2, alto_pantalla // 2)
radio_circulo = 20
ruta = []

# Función para dibujar el círculo sin relleno
def dibujar_circulo(ventana, centro, radio):
    pygame.draw.circle(ventana, color_dibujo, centro, radio, 1)  # El último argumento define el grosor de la línea

# Función para mover el círculo a lo largo de la ruta y borrar la línea tras él
def mover_circulo(ventana, ruta):
    if len(ruta) >= 2:  # Asegura que haya al menos dos puntos en la ruta
        for i, punto in enumerate(ruta):
            ventana.fill(color_pantalla)
            if i < len(ruta) - 1:
                pygame.draw.lines(ventana, color_dibujo, False, ruta[i + 1:], 1)  # Dibuja el resto de la ruta
            dibujar_circulo(ventana, punto, radio_circulo)
            pygame.display.flip()
            pygame.time.delay(50)

# Bucle principal
ejecutando = True
dibujando_ruta = False
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            ruta = [evento.pos]  # Reinicia la ruta con el punto inicial del clic
            dibujando_ruta = True
        elif evento.type == pygame.MOUSEBUTTONUP and dibujando_ruta:
            dibujando_ruta = False
            if len(ruta) >= 2:  # Verifica de nuevo antes de mover el círculo
                mover_circulo(ventana, ruta)
            ruta = []  # Reinicia la ruta
        elif evento.type == pygame.MOUSEMOTION and dibujando_ruta:
            ruta.append(evento.pos)
            if len(ruta) >= 2:  # Verifica antes de intentar dibujar la ruta
                ventana.fill(color_pantalla)
                pygame.draw.lines(ventana, color_dibujo, False, ruta, 1)  # Dibuja la ruta
            dibujar_circulo(ventana, circulo_pos, radio_circulo)  # Mantiene el círculo visible
            pygame.display.flip()

pygame.quit()


