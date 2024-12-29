import pygame
import sys

# Inicialización
pygame.init()
screen = pygame.display.set_mode((800, 600))  # Crear ventana gráfica
pygame.display.set_caption("Modo Gráfico en Pygame")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  # Fondo negro
    pygame.draw.rect(screen, RED, (200, 150, 400, 300))  # Dibujar un rectángulo rojo
    pygame.display.flip()  # Actualizar la pantalla

pygame.quit()
sys.exit()
