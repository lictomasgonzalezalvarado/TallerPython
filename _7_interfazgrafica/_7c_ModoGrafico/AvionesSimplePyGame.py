import pygame
import sys

# Configuración inicial de Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Crear la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Aviones Multijugador")

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Fuente para los textos
font = pygame.font.Font(None, 36)

# Función para mostrar texto en la pantalla
def draw_text(surface, text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

# Clase para los jugadores
class Player:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = color
        self.speed = 5
        self.bullets = []

    def move(self, keys, up, down, left, right):
        if keys[up]:
            self.rect.y -= self.speed
        if keys[down]:
            self.rect.y += self.speed
        if keys[left]:
            self.rect.x -= self.speed
        if keys[right]:
            self.rect.x += self.speed

    def shoot(self):
        bullet = pygame.Rect(self.rect.centerx - 5, self.rect.y - 10, 10, 20)
        self.bullets.append(bullet)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        for bullet in self.bullets:
            pygame.draw.rect(surface, WHITE, bullet)

    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet.y -= 10
            if bullet.y < 0:
                self.bullets.remove(bullet)

# Clase para el menú
class Menu:
    def __init__(self):
        self.options = ["Jugar", "Ayuda", "Salir"]
        self.selected = 0

    def draw(self, surface):
        surface.fill(BLACK)
        for i, option in enumerate(self.options):
            color = WHITE if i == self.selected else (100, 100, 100)
            draw_text(surface, option, WIDTH // 2 - 50, HEIGHT // 2 + i * 40, color)

    def navigate(self, direction):
        self.selected = (self.selected + direction) % len(self.options)

# Función para mostrar la ayuda
def show_help():
    running = True
    while running:
        screen.fill(BLACK)
        draw_text(screen, "Instrucciones del Juego:", 50, 50)
        draw_text(screen, "Jugador 1: Mover con W/A/S/D, disparar con Espacio.", 50, 100)
        draw_text(screen, "Jugador 2: Mover con Flechas, disparar con Enter.", 50, 150)
        draw_text(screen, "Presiona Esc para volver al menú.", 50, 200)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

# Juego principal
def game_loop():
    player1 = Player(100, HEIGHT - 100, RED)
    player2 = Player(WIDTH - 140, HEIGHT - 100, BLUE)

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player1.shoot()
                if event.key == pygame.K_RETURN:
                    player2.shoot()

        keys = pygame.key.get_pressed()
        player1.move(keys, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
        player2.move(keys, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

        player1.update_bullets()
        player2.update_bullets()

        player1.draw(screen)
        player2.draw(screen)

        pygame.display.flip()
        clock.tick(60)

# Menú principal
def main():
    menu = Menu()
    running = True

    while running:
        menu.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    menu.navigate(1)
                if event.key == pygame.K_UP:
                    menu.navigate(-1)
                if event.key == pygame.K_RETURN:
                    if menu.selected == 0:  # Jugar
                        game_loop()
                    elif menu.selected == 1:  # Ayuda
                        show_help()
                    elif menu.selected == 2:  # Salir
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    main()
