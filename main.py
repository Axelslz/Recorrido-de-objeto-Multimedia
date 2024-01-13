import pygame
import math

ancho_pantalla = 800
alto_pantalla = 600

# Crea una ventana de 800x600 píxeles
ventana = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
# Establece el color de fondo
color_pantalla = (255, 255, 255)
color_dibujo = (0, 0, 0)

# Variables para controlar el estado
circulos = []
lineas = []
dibujando_circulo = False
dibujando_linea = False
punto_inicial_linea = None

# Definir una función para calcular el radio
def obtener_radio(ca, co):
    return math.sqrt(ca**2 + co**2)

# Bucle principal
while True:
    # Obtiene los eventos del usuario
    eventos = pygame.event.get()
    # Maneja los eventos
    for evento in eventos:
        if evento.type == pygame.QUIT:
            # Sale del bucle y termina el programa si se cierra la ventana
            pygame.quit()
            exit()

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Clic izquierdo
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:  # Verifica si se mantiene presionado Ctrl
                    # Si se mantiene presionado Ctrl, añade un círculo a la lista de círculos
                    x, y = evento.pos
                    circulos.append((x, y))
                    dibujando_circulo = True
                elif keys[pygame.K_SPACE]:  # Verifica si se presiona la tecla de espacio
                    # Si se presiona la tecla de espacio, inicia la creación de líneas
                    punto_inicial_linea = evento.pos
                    dibujando_linea = True

        elif evento.type == pygame.MOUSEMOTION:
            if dibujando_circulo:
                # Si se está dibujando un círculo, actualiza la ventana
                ventana.fill(color_pantalla)
                for circulo in circulos:
                    pygame.draw.circle(ventana, color_dibujo, circulo, 10, 1)
            elif dibujando_linea:
                # Si se está dibujando una línea, actualiza la ventana
                ventana.fill(color_pantalla)
                for circulo in circulos:
                    pygame.draw.circle(ventana, color_dibujo, circulo, 10, 1)
                for linea in lineas:
                    pygame.draw.line(ventana, color_dibujo, linea[0], linea[1], 2)
                pygame.draw.line(ventana, color_dibujo, punto_inicial_linea, evento.pos, 2)

        elif evento.type == pygame.MOUSEBUTTONUP:
            if dibujando_circulo:
                dibujando_circulo = False
            elif dibujando_linea:
                dibujando_linea = False
                lineas.append((punto_inicial_linea, evento.pos))

    # Actualiza la ventana fuera del bucle de eventos
    pygame.display.update()
