import pygame
from math import sin, cos, pi
from time import sleep
ancho = 1000
alto = 1000
screen = pygame.display.set_mode((ancho, alto))
running = True

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRIS = (100, 100, 100)
ROJO = (255, 10, 10)


def lineas(punto0, punto1, redondez):
    x0, y0 = punto0
    x1, y1 = punto1

    # Linea vertical izquierda
    pygame.draw.aaline(screen, WHITE, (x0, y0+(redondez*(y1-y0)/2)), (x0, y1-(redondez*(y1-y0)/2)))

    # Linea vertical derecha
    pygame.draw.aaline(screen, WHITE, (x1, y0+(redondez*(y1-y0)/2)), (x1, y1-(redondez*(y1-y0)/2)))

    # Linea horizontal superior
    pygame.draw.aaline(screen, WHITE, (x0+(redondez*(x1-x0)/2), y0), (x1-(redondez*(x1-x0)/2), y0))

    # Linea horizontal inferior
    pygame.draw.aaline(screen, WHITE, (x0+(redondez*(x1-x0)/2), y1), (x1-(redondez*(x1-x0)/2), y1))


def bordes(punto0, punto1, redondez):
    x0, y0 = punto0
    x1, y1 = punto1
    cantidad_rectas = 8

    # Centro auxiliar inferior derecho
    centro0x, centro0y = x1-(redondez*(x1-x0)/2), y1-(redondez*(y1-y0)/2)
    pygame.draw.aaline(screen, WHITE, (centro0x, centro0y), (centro0x, centro0y))

    for i in range(0, cantidad_rectas):
        # Calculamos los cuatro puntos para la siguiente recta.
        angulo1 = i * (0.5*pi/cantidad_rectas)
        angulo2 = (i+1) * (0.5*pi/cantidad_rectas)
        print(f'Angulos: {angulo1} {angulo2}')
        a = centro0x + (redondez*(x1-x0)/2)*cos(angulo1)
        b = centro0y + (redondez*(y1-y0)/2)*sin(angulo1)
        c = centro0x + (redondez*(x1-x0)/2)*cos(angulo2)
        d = centro0y + (redondez*(y1-y0)/2)*sin(angulo2)
        # if i == 0:
        pygame.draw.aaline(screen, WHITE, (a, b), (c, d))

    # Centro auxiliar inferior izquierdo
    centro0x, centro0y = x0+(redondez*(x1-x0)/2), y1-(redondez*(y1-y0)/2)
    pygame.draw.aaline(screen, WHITE, (centro0x, centro0y), (centro0x, centro0y))

    for i in range(0, cantidad_rectas):
        # Calculamos los cuatro puntos para la siguiente recta.
        angulo1 = 0.5*pi + i * (0.5*pi/cantidad_rectas)
        angulo2 = 0.5*pi + (i+1) * (0.5*pi/cantidad_rectas)
        print(f'Angulos: {angulo1} {angulo2}')
        a = centro0x + (redondez*(x1-x0)/2)*cos(angulo1)
        b = centro0y + (redondez*(y1-y0)/2)*sin(angulo1)
        c = centro0x + (redondez*(x1-x0)/2)*cos(angulo2)
        d = centro0y + (redondez*(y1-y0)/2)*sin(angulo2)
        # if i == 0:
        pygame.draw.aaline(screen, WHITE, (a, b), (c, d))

    # Centro auxiliar superior izquierdo
    centro0x, centro0y = x0+(redondez*(x1-x0)/2), y0+(redondez*(y1-y0)/2)
    pygame.draw.aaline(screen, WHITE, (centro0x, centro0y), (centro0x, centro0y))

    for i in range(0, cantidad_rectas):
        # Calculamos los cuatro puntos para la siguiente recta.
        angulo1 = pi + i * (0.5*pi/cantidad_rectas)
        angulo2 = pi + (i+1) * (0.5*pi/cantidad_rectas)
        print(f'Angulos: {angulo1} {angulo2}')
        a = centro0x + (redondez*(x1-x0)/2)*cos(angulo1)
        b = centro0y + (redondez*(y1-y0)/2)*sin(angulo1)
        c = centro0x + (redondez*(x1-x0)/2)*cos(angulo2)
        d = centro0y + (redondez*(y1-y0)/2)*sin(angulo2)
        # if i == 0:
        pygame.draw.aaline(screen, WHITE, (a, b), (c, d))

    # Centro auxiliar superior derecho
    centro0x, centro0y = x1-(redondez*(x1-x0)/2), y0+(redondez*(y1-y0)/2)
    pygame.draw.aaline(screen, WHITE, (centro0x, centro0y), (centro0x, centro0y))

    for i in range(0, cantidad_rectas):
        # Calculamos los cuatro puntos para la siguiente recta.
        angulo1 = 1.5*pi + i * (0.5*pi/cantidad_rectas)
        angulo2 = 1.5*pi + (i+1) * (0.5*pi/cantidad_rectas)
        print(f'Angulos: {angulo1} {angulo2}')
        a = centro0x + (redondez*(x1-x0)/2)*cos(angulo1)
        b = centro0y + (redondez*(y1-y0)/2)*sin(angulo1)
        c = centro0x + (redondez*(x1-x0)/2)*cos(angulo2)
        d = centro0y + (redondez*(y1-y0)/2)*sin(angulo2)
        # if i == 0:
        pygame.draw.aaline(screen, WHITE, (a, b), (c, d))


def rectangulo_con_bordes(punto0, punto1, redondez):
    pass


if __name__ == '__main__':
    while running:
        punto0 = (100, 100)
        punto1 = (800, 400)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        screen.fill(BLACK)
        lineas(punto0, punto1, 0.2)
        bordes(punto0, punto1, 0.2)
        pygame.display.flip()
