
import pygame
import math

ancho_pantalla = 800
alto_pantalla = 600

ventana = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
color_pantalla = (255, 255, 255)
color_dibujo = (0, 0, 0)

circulos = []
lineas = []
dibujando_circulo = False
dibujando_linea = False
punto_inicial_linea = None

reloj = pygame.time.Clock()
FPS = 60

def obtener_radio(ca, co):
    return math.sqrt(ca**2 + co**2)

while True:
    reloj.tick(FPS)

    ventana.fill(color_pantalla)

    for circulo in circulos:
        x, y, radio = circulo
        pygame.draw.circle(ventana, color_dibujo, (x, y), radio, 1)

    for linea in lineas:
        pygame.draw.line(ventana, color_dibujo, linea[0], linea[1], 2)

    if dibujando_circulo:
        x, y = pygame.mouse.get_pos()
        radio_temporal = int(obtener_radio(x - circulos[-1][0], y - circulos[-1][1]))
        circulos[-1] = (circulos[-1][0], circulos[-1][1], radio_temporal)
        pygame.draw.circle(ventana, color_dibujo, (circulos[-1][0], circulos[-1][1]), radio_temporal, 1)

    if dibujando_linea:
        for linea in lineas:
            pygame.draw.line(ventana, color_dibujo, linea[0], linea[1], 2)
        x, y = pygame.mouse.get_pos()
        pygame.draw.line(ventana, color_dibujo, punto_inicial_linea, (x, y), 2)

        if dibujando_circulo:
            # Calcular la posición del círculo a lo largo de la línea
            distancia_total = math.sqrt((linea[0][0] - linea[1][0])**2 + (linea[0][1] - linea[1][1])**2)
            distancia_actual = math.sqrt((punto_inicial_linea[0] - x)**2 + (punto_inicial_linea[1] - y)**2)
            porcentaje_recorrido = distancia_actual / distancia_total

            # Calcular las coordenadas del círculo en la línea
            x_circulo = int(linea[0][0] + porcentaje_recorrido * (linea[1][0] - linea[0][0]))
            y_circulo = int(linea[0][1] + porcentaje_recorrido * (linea[1][1] - linea[0][1]))

            radio_temporal = int(obtener_radio(x - x_circulo, y - y_circulo))
            circulos[-1] = (x_circulo, y_circulo, radio_temporal)
            pygame.draw.circle(ventana, color_dibujo, (x_circulo, y_circulo), radio_temporal, 1)

    pygame.display.update()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
                    x, y = evento.pos
                    radio_temporal = 10
                    circulos = []
                    circulos.append((x, y, radio_temporal))
                    dibujando_circulo = True
                elif keys[pygame.K_SPACE]:
                    punto_inicial_linea = evento.pos
                    lineas = []
                    dibujando_linea = True
        elif evento.type == pygame.MOUSEBUTTONUP:
            if dibujando_circulo:
                dibujando_circulo = False
            elif dibujando_linea:
                dibujando_linea = False
                lineas.append((punto_inicial_linea, pygame.mouse.get_pos()))
